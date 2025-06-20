from abc import ABC, abstractmethod

class LevelBase(ABC):
    """
    Clase base abstracta para niveles de idioma.
    """
    @abstractmethod
    def get_level_name(self):
        pass

class Level(LevelBase):
    """
    Representa un nivel de idioma concreto.
    """
    def __init__(self, name: str):
        self.name = name

    def get_level_name(self):
        return self.name