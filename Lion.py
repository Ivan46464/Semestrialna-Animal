from Animal import Animal
import re
from Exception import *


class Lion(Animal):
    pregnant = False

    def __init__(self, name, age, species, mane_color, predatory, male):
        super().__init__(name, age, species)
        self.mane_color = mane_color
        self.predatory = predatory
        self.male = male

    def eat(self, food):
        print("The lion is eating " + food)

    def make_sound(self):
        print("Roar")

    def mate_with(self, lion):
        if self.male == lion.male:
            print("The same gender lions cannot be mated.")
        else:
            print("The lion " + self.name + "has mated with " + lion.name)
            if not self.male:
                self.pregnant = True
            else:
                lion.pregnant = True

    def give_birth(self, animals):
        if self.male:
            print("The lion is male so cannot give birth.")
        else:
            if self.pregnant:
                name_pattern = re.compile("^[A-Z][-a-z]{3,20}")
                while True:
                    try:
                        name = input("Input name: ")
                        if name_pattern.match(name):
                            break
                        else:
                            raise invalid_name
                    except invalid_name:
                        print("Enter a valid name.")
                colors = [
                    'Blonde', 'Sandy', 'Dark Brown', 'Black', 'Reddish-Brown', 'Blonde with Dark Tips']
                while True:
                    try:
                        mane_color: str = input("Input mane color: ")
                        mane = False
                        for x in colors:
                            if mane_color == x:
                                mane = True
                        if mane:
                            break
                        else:
                            raise invalid_mane_color
                    except invalid_mane_color:
                        print("Input valid color.")
                while True:
                    try:
                        male = input("Input M for male and F for female: ")

                        if str(male) == "M":
                            gender = True
                        elif str(male) == "F":
                            gender = False
                        else:
                            gender = None
                        if gender is None:
                            raise invalid_gender
                        else:
                            break
                    except invalid_gender:
                        print("Enter M or F.")
                lion = Lion(name, 0, "Lion", mane_color, True, gender)
                animals.append(lion)

            else:
                print("The lioness has not mated yet so she cannot give birth.")
