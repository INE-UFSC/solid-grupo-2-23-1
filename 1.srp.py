"""
Single Responsibility Principle

Uma classe deve ter somente uma responsabilidade
ou
Uma classe deve ter somente um motivo para mudar
"""

class Animal:
    def __init__(self, name: str, db: AnimalDB):
        self.__name = name
        self.__db = db

    @property
    def name(self) -> str:
        return self.__name

    def save(self):
        self.__db.save(self)

# Banco de dados contendo vários animais.
class AnimalDB:
    def __init__(self):
        pass

    def save(self, animal: Animal):
        # Salva no banco de dados.
        pass
