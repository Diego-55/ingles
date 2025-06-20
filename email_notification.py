from abc import ABC, abstractmethod

class Notifiable(ABC):
    """
    Clase base abstracta para objetos notificables.
    """
    @abstractmethod
    def notify(self, message: str):
        pass

class EmailNotification(Notifiable):
    """
    Envía notificaciones por correo electrónico.
    """
    def notify(self, message: str):
        return f"Email sent: {message}"