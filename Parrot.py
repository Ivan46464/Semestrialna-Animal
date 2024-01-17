from Animal import Animal


class Parrot(Animal):
    vocabulary = []

    def __init__(self, name, age, species, type_of, feather_color):
        super().__init__(name, age, species)
        self.feather_color = feather_color
        self.type_of = type_of

    def make_sound(self):
        print("Kya")

    def eat(self, food):
        print("The parrot eat " + food)

    @staticmethod
    def imitate_human_speech():
        print('Word')

    def learn_word(self):
        word = input("What word to learn: ")
        self.vocabulary.append(word)
        print("The parrot has learned the word: ")
