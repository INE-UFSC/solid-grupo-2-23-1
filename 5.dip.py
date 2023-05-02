"""
Dependency Inversion Principle

Dependências devem ser feitas sobre abstrações, não sobre implementações concretas 

"""


class Entity:
    def __init__(self, name, hp, speed):
        self.stats = StatsReporter(self)
        self.__name = name
        self.__hp = hp
        self.__speed = speed 

    def hp(self):
        return self.__hp

    def name(self):
        return self.__name

class Player(Entity):
    def __init__(self, name):
        super.__init__(name, 100, 1)

class StatsReporter:
    def __init__(self, char: Entity):
        self.char = char

    def report(self):
        print(f'Name:{self.char.name()}')
        print(f'HP:{self.char.hp()}')
