from Animal import Animal


class Parrot(Animal):
    vocabulary = []

    def __init__(self, name, age, species, feather_color):
        super().__init__(name, age, species)
        self.feather_color = feather_color

    def make_sound(self):
        print("Kya")

    def eat(self, food):
        print("The parrot eat " + food)

    def imitate_human_speech(self):
        pass

    def learn_word(self):
        word = input("What word to learn: ")
        self.vocabulary.append(word)
        print("The parrot has learned the word: ")
