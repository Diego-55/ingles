from abc import ABC, abstractmethod

class Material(ABC):
    """
    Clase base abstracta para materiales educativos.
    """
    @abstractmethod
    def get_type(self):
        pass

class Dictionary(Material):
    """
    Representa un material tipo diccionario.
    """
    def __init__(self, language: str):
        self.language = language

    def get_type(self):
        return "Dictionary"