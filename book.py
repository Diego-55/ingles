from abc import ABC, abstractmethod

class Material(ABC):
    """
    Clase base abstracta para materiales educativos.
    """
    @abstractmethod
    def get_type(self):
        pass

class Book(Material):
    """
    Representa un material tipo libro.
    """
    def __init__(self, title: str):
        self.title = title

    def get_type(self):
        return "Book"