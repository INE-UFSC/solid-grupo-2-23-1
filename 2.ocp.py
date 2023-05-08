"""
Open-Closed Principle

Classes devem estar fechadas para modificação, mas abertas para extensão
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def make_sound(self):
        print('roar')

class Mouse(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def make_sound(self):
        print('squeak')


animals = [
    Lion('Simba'),
    Mouse('Mickey')
]

def animal_sound(animals: list):
    for animal in animals:
        animal.make_sound()

animal_sound(animals)


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
