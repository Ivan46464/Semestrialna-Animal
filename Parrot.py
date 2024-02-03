from Animal import Animal

basic_words = [
    "Apple", "Ball", "Cat", "Dog", "Elephant", "Fish", "Goat", "Hat", "Ice", "Jar",
    "Kite", "Lion", "Moon", "Nest", "Orange", "Pen", "Queen", "Rabbit", "Sun", "Tree",
    "Umbrella", "Violin", "Watch", "Xylophone", "Yak", "Zebra", "Ant", "Banana", "Car",
    "Duck", "Egg", "Flower", "Guitar", "House", "Insect", "Jug", "Kangaroo", "Lemon",
    "Mango", "Nose", "Octopus", "Piano", "Quilt", "Rainbow", "Snake", "Tiger", "Umbrella",
    "Volcano", "Watermelon", "X-ray", "Yacht", "Zoo", "Book", "Chair", "Table", "Door",
    "Window", "Bed", "Cup", "Plate"
]


class Parrot(Animal):
    def __init__(self, name, age, species, type_of, feather_color):
        super().__init__(name, age, species)
        self.feather_color = feather_color
        self.type_of = type_of
        self.vocabulary = Parrot.vocabulary_set(age, type_of)

    @staticmethod
    def vocabulary_set(age, type_of):
        import pandas as pd
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LinearRegression
        import random
        df = pd.read_csv("Parrot.csv")
        df['parrot_name'] = df['parrot_name'].replace({'Budgerigar': 1, 'Eclectus': 2, 'Rose-ringed parakeet': 3})
        types_of = {'Budgerigar': 1, 'Eclectus': 2, 'Rose-ringed parakeet': 3}
        multi_lin = LinearRegression()
        feature_names = ["age", "parrot_name"]
        X = df[feature_names]
        y = df["number_of_words"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=6)
        multi_lin.fit(X_train, y_train)
        number_of_type = 0
        for i, x in enumerate(types_of.keys()):
            if type_of == x:
                number_of_type = i + 1

        parrot = [[age, number_of_type]]
        parrot_pred = multi_lin.predict(parrot)
        num_of_words = round(parrot_pred[0])
        voc = []
        while len(voc) < num_of_words:
            random_element = random.choice(basic_words)
            if random_element not in voc:
                voc.append(random_element)
        return voc

    def make_sound(self):
        print("Kya")

    def eat(self, food):
        print("The parrot eat " + food)

    def imitate_human_speech(self):
        import random
        print(random.choice(self.vocabulary))
        print(len(self.vocabulary))

    def learn_word(self):
        word = input("What word to learn: ")
        self.vocabulary.append(word)
        print("The parrot has learned the word: ")


