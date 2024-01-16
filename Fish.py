from Animal import Animal


class Fish(Animal):

    def __init__(self, name, age, species, water_type, predatory, lay_eggs):
        super().__init__(name, age, species)
        self.water_type = water_type
        self.predatory = predatory
        self.lay_eggs = lay_eggs

    def make_sound(self):
        print("Buble-buble")

    def eat(self, food):
        print("The fish eat " + food)

    @staticmethod
    def swim():
        print("The fish is swimming")

    def lay_eggs(self, fish):
        pass
