from Animal import Animal
import re
from Exception import *


class Lion(Animal):
    pregnant = False

    @staticmethod
    def alpha(age, weight, mane_color, health, sex):
        if sex:
            import pandas as pd
            from sklearn.preprocessing import StandardScaler
            from sklearn.model_selection import train_test_split
            from sklearn.ensemble import RandomForestClassifier
            import numpy as np
            df = pd.read_csv("Lion_alpha.csv")
            np.random.seed(42)
            df["mane_color"] = df["mane_color"].replace({"Blonde": 1, "Dark Brown": 2,
                                                         "Reddish-Brown": 3, "Black": 4, "Blonde with Dark Tips": 5,
                                                         "Sandy": 6})
            df["health"] = df["health"].replace({"Poor": 1, "Good": 2, "Great": 3, "Excelent": 4})
            X = df[["age", "weight", "mane_color", "health"]]
            y = df["alpha"]
            scaler = StandardScaler()
            X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=8, test_size=0.3)
            X_train = scaler.fit_transform(X_train)
            X_test = scaler.transform(X_test)
            model = RandomForestClassifier(max_depth=7, class_weight="balanced")
            model.fit(X_train, y_train)
            color_num = 0
            mane_colors = {"Blonde": 1, "Dark Brown": 2,"Reddish-Brown": 3, "Black": 4, "Blonde with Dark Tips": 5, "Sandy": 6}
            healths = {"Poor": 1, "Good": 2, "Great": 3, "Excelent": 4}
            if mane_color in mane_colors:
                color_num = mane_colors[mane_color]
            health_num = 0
            if health in healths:
                health_num = healths[health]
            inputs = [[age, weight, color_num, health_num]]
            inputs_scaled = scaler.transform(inputs)
            is_alpha = model.predict(inputs_scaled)


            return is_alpha
        else:
            return 0

    def __init__(self, name, age, weight, health, species, mane_color, predatory, male):
        super().__init__(name, age, species)
        self.mane_color = mane_color
        self.predatory = predatory
        self.male = male
        self.weight = weight
        self.health = health
        self.is_alpha = Lion.alpha(age, weight, mane_color, health, male)
        if self.is_alpha == 1:
            self.pack = []

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

    def add_pack_if_alpha(self, animals):
        if self.male:
            if self.is_alpha == 1:

                print(self.name + " is alpha.")
                while True:
                    print("1.Add pack")
                    print("2.Exit")
                    choice = int(input("Pick: "))
                    match choice:
                        case 1:
                            lions = list(filter(lambda lion: lion.species == "Lion", animals))
                            female_lions = list(filter(lambda lioness: not lioness.male, lions))
                            print("Available lioness: ")
                            for x in female_lions:
                                print(x.name)
                            name = str(input("Add one: "))
                            have = False
                            for x in female_lions:
                                if x.name == name:
                                    if name not in self.pack:
                                        self.pack.append(x)
                                    have = True
                            if not have:
                                print("There is no such lioness.")
                        case 2:
                            break

            else:
                print("The lion is not alpha ")
        else:
            print("The lion is female")

