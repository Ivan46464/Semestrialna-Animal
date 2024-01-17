import Parrot
import Lion
import Fish
from Exception import *
import re


class Zoo:

    @staticmethod
    def add_lion(animals):
        while True:
            try:
                age = input("Input age: ")
                if age.isdigit():
                    age = int(age)
                    if age <= 0:
                        raise invalid_age
                    break
                else:
                    raise invalid_age
            except invalid_age:
                print("Enter a valid age.")
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

        lion = Lion.Lion(name, age, "Lion", mane_color, True, gender)
        animals.append(lion)

    @staticmethod
    def add_parrot(animals):
        while True:
            try:
                age = input("Input age: ")
                if age.isdigit():
                    age = int(age)
                    if age <= 0:
                        raise invalid_age
                    break
                else:
                    raise invalid_age
            except invalid_age:
                print("Enter a valid age.")
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
            "Red", "Green", "Blue", "Yellow", "Purple", "Orange", "Pink", "Brown",
            "Cyan", "Magenta", "Turquoise", "Lime", "Indigo", "Teal", "Maroon",
            "Olive", "Violet", "Gold", "Silver", "Gray"]
        while True:
            try:
                feather_color: str = input("Input feather color: ")
                mane = False
                for x in colors:
                    if feather_color == x:
                        mane = True
                if mane:
                    break
                else:
                    raise invalid_mane_color
            except invalid_mane_color:
                print("Input valid color.")
        parrot = Parrot.Parrot(name, age, "Parrot", feather_color)
        animals.append(parrot)

    @staticmethod
    def add_fish(animals):

        while True:
            try:
                age = input("Input age: ")
                if age.isdigit():
                    age = int(age)
                    if age <= 0:
                        raise invalid_age
                    break
                else:
                    raise invalid_age
            except invalid_age:
                print("Enter a valid age.")
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
        while True:
            try:
                water_type: str = input("Input water type: ")
                if water_type != "Salt" or water_type != "Freshwater":
                    break
                else:
                    raise invalid_water_type
            except invalid_name:
                print("Enter a water type.")

        while True:
            try:
                predatory = input("Input is it predatory (Y or N): ")

                if str(predatory) == "Y":
                    ispredatory = True
                elif str(predatory) == "N":
                    ispredatory = False
                else:
                    ispredatory = None
                if ispredatory is None:
                    raise invalid_predatory
                else:
                    break
            except invalid_predatory:
                print("You should choose between Y or N")
        while True:
            try:
                eggs = input("Input does it lay eggs (Y or N): ")

                if str(eggs) == "Y":
                    lay_eggs = True
                elif str(eggs) == "N":
                    lay_eggs = False
                else:
                    lay_eggs = None
                if lay_eggs is None:
                    raise invalid_lay_eggs
                else:
                    break
            except invalid_lay_eggs:
                print("You should write Y or N")

        fish = Fish.Fish(name, age, "Fish", water_type, ispredatory, lay_eggs)
        animals.append(fish)

    @staticmethod
    def lion_methods(animals):
        lion_instance = None

        lions = filter(lambda lion1: lion1.species == "Lion", animals)
        lions_list = list(lions)
        if not lions_list:
            print("There are no lions so you cannot continue.")
            return
        else:
            lion_name = str(input("What is the name of the lion you are searching for: "))
            for x in lions_list:
                if x.name == lion_name:
                    lion_instance = x
            if lion_instance is None:
                print("There is no lion with such name.")
            while lion_instance is not None:
                print("1.Make sound")
                print("2.Eat")
                print("3.Mate with")
                print("4.Give birth")
                print("5.Exit")
                choice = int(input("Input your choice: "))
                match choice:
                    case 1:
                        lion_instance.make_sound()
                    case 2:
                        food = input("Input what food to eat: ")
                        lion_instance.eat(food)
                    case 3:
                        lion_to_mate = None
                        lions = []
                        for x in animals:
                            if x.species == "Lion":
                                lions.append(x)
                        for x in lions:
                            if len(lions) == 1:
                                print("There is only one or non lion`s so it cannot mate with anyone.")
                            else:
                                print("The available lions are: " + x.name)
                                name_of_lion = input("What is the name of the lion: ")
                                for lion in lions:
                                    if lion.name == name_of_lion:
                                        lion_to_mate = lion

                                lion_instance.mate_with(lion_to_mate)
                    case 4:
                        lion_instance.give_birth(animals)
                    case 5:
                        break

    @staticmethod
    def parrot_methods(animals):
        parrot_instance = None

        parrots = filter(lambda parrot: parrot.species == "Parrot", animals)
        parrots_list = list(parrots)
        if not parrots_list:
            print("There are no parrots so you cannot continue.")
            return
        else:
            parrot_name = str(input("What is the name of the parrot you are searching for: "))
            for x in parrots_list:
                if x.name == parrot_name:
                    parrot_instance = x
            if parrot_instance is None:
                print("There is no lion with such name.")
            else:
                while parrot_instance is not None:
                    print("1.Make sound")
                    print("2.Eat")
                    print("3.Imitate human speech")
                    print("4.Learn word")
                    print("5.Exit")
                    choice = int(input("Input your choice: "))
                    match choice:
                        case 1:
                            parrot_instance.make_sound()
                        case 2:
                            food = input("Input what food to eat: ")
                            parrot_instance.eat(food)
                        case 3:
                            parrot_instance.imitate_human_speech()
                        case 4:
                            parrot_instance.learn_word()
                        case 5:
                            break

    @staticmethod
    def fish_methods(animals):
        fish_instance = None

        fish = filter(lambda fish1: fish1.species == "Fish", animals)
        fish_list = list(fish)
        if not fish_list:
            print("There are no fishes so you cannot continue.")
            return
        else:
            fish_name = str(input("What is the name of the fish you are searching for: "))
            for x in fish_list:
                if x.name == fish_name:
                    fish_instance = x
            if fish_instance is None:
                print("There is no fish with such name.")
            else:
                while fish_instance is not None:
                    print("1.Make sound")
                    print("2.Eat")
                    print("3.Swim")
                    print("4.Lay eggs")
                    print("5.Exit")
                    choice = int(input("Input your choice: "))
                    match choice:
                        case 1:
                            fish_instance.make_sound()
                        case 2:
                            food = input("Input what food to eat: ")
                            fish_instance.eat(food)
                        case 3:
                            fish_instance.swim()
                        case 4:
                            fish_instance.lay_eggs()
                        case 5:
                            break

    @staticmethod
    def delete_animal(animals):
        import logging
        import sys
        logger = logging.getLogger(__name__)
        stream_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(stream_handler)
        lions = filter(lambda lion: lion.species == "Lion", animals)
        lion_list = list(lions)
        parrots = filter(lambda parrot: parrot.species == "Parrot", animals)
        parrots_list = list(parrots)
        fish = filter(lambda fish1: fish1.species == "Fish", animals)
        fish_list = list(fish)
        animal_type = str(input("What type of animal to delete: "))
        if animal_type != "Lion" or animal_type != "Parrot" or animal_type != "Fish":

            if animal_type == "Lion":
                list_to_use = lion_list
            elif animal_type == "Fish":
                list_to_use = fish_list
            else:
                list_to_use = parrots_list
            animal_to_del = str(input("Input the name of the animal: "))
            del_an = False
            for animal in list_to_use:
                if animal.name == animal_to_del:
                    animals.remove(animal)
                    del_an = True
            if del_an:
                logger.info("The animal has been deleted")
            else:
                logger.warning("We dont have animal of type " + animal_type + " with such name.")
        else:
            logger.warning("There is no animal with this species in our shop.")

    @staticmethod
    def print_available(animals):
        for animal in animals:
            print("Name: " + animal.name + " ,Species: " + animal.species)
