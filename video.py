from abc import ABC, abstractmethod

class Material(ABC):
    """
    Clase base abstracta para materiales educativos.
    """
    @abstractmethod
    def get_type(self):
        pass

class Video(Material):
    """
    Representa un material tipo video.
    """
    def __init__(self, title: str):
        self.title = title

    def get_type(self):
        return "Video"