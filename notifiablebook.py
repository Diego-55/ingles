from abc import ABC, abstractmethod

class Material(ABC):
    """
    Clase base abstracta para materiales educativos.
    """
    @abstractmethod
    def get_type(self):
        pass

class Notifiable(ABC):
    """
    Clase base abstracta para objetos notificables.
    """
    @abstractmethod
    def notify(self, message: str):
        pass

class NotifiableBook(Material, Notifiable):
    """
    Libro digital que es material educativo y puede enviar notificaciones.
    """
    def __init__(self, title, submaterials=None):
        self.title = title
        self.submaterials = submaterials if submaterials else []

    def get_type(self):
        return "NotifiableBook"

    def notify(self, message):
        return f"Notificación del libro '{self.title}': {message}"