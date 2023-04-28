"""
Interface Segregation Principle
Crie interfaces que são específicas. Clientes não devem depender de interfaces que eles não usarão
"""
from abc import ABC

# Removi os métodos desnecessários em IJanela e deixei somente os necessários
# para as duas classes.

class IJanela(ABC):
    def minimizar(self):
        raise NotImplementedError

    def fechar(self):
        raise NotImplementedError


class JanelaTamanhoFixo(IJanela):
    def minimizar(self):
        pass
    
    def fechar(self):
        pass

    def mostrar_menu(self):
        pass
    

class JanelaSemMenu(IJanela):
    def minimizar(self):
        pass

    def fechar(self):
        pass

    def maximizar(self):
        pass
