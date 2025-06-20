from abc import ABC, abstractmethod

class Notifiable(ABC):
    """
    Interface for notification systems.
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