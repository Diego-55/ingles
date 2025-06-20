from abc import ABC, abstractmethod

class Notifiable(ABC):
    """
    Clase base abstracta para objetos notificables.
    """
    @abstractmethod
    def notify(self, message: str):
        pass

class SMSNotification(Notifiable):
    """
    Implementación concreta de Notifiable para SMS.
    """
    def notify(self, message: str):
        return f"SMS enviado: {message}"