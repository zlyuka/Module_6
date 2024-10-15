class Animal:

    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name


class Plant:

    def __init__(self, name):
        self.edible = False
        self.name = name


class Mammal(Animal):
    def eat(self, food):
        pass

class Predator(Animal):
    def eat(self, food):
        pass

class Flower(Plant):
    edible = True
    pass

class Fruit(Plant):
    edible = True
    pass