"""
Open-Closed Principle

Classes devem estar fechadas para modificação, mas abertas para extensão
"""
from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name: str, sound: str):
        self.name = name
        self.sound = sound
        self.animals = []
        
    
    @property
    def get_name(self) -> str:
        pass

    @property
    def get_sound(self):
        return self.sound

    
    def make_sound(self):
        print(self.sound)

    def add(self):
        self.animals.append(self)

class Lista:
    def __init__(self):
        self.animals = []

    def add(self, animal:Animal):
        self.animals.append(animal)


def animal_sound(animals: list):
    for animal in animals:
        animal.make_sound()

#animal_sound(animals)


"""
Outro exemplo:

Imagine que você tem uma loja que dá desconto de 20% aos seus clientes favoritos
usando essa classe abaixo. Quando você decide dar 40% de desconto a clientes VIP,
você decide mudar a classe da seguinte forma:
"""

class Cliente(ABC):
    def __init__(self, nome: str):
        self.__nome = nome
    
    @abstractmethod
    def desconto(self):
        pass
        
class ClienteFAV(Cliente):
    def __init__(self, nome: str):
        super().__init__(nome)

    def desconto(self, price):
        return price * 0.8

class ClienteVIP(Cliente):
    def __init__(self, nome: str):
        super().__init__(nome)

    def desconto(self, price):
        return price * 0.6

joao = ClienteFAV("João")
alfeu = ClienteVIP("Alfeu")

venda1 = joao.desconto(700)
print(venda1)

venda2 = alfeu.desconto(600)
print(venda2)