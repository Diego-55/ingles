from abc import ABC, abstractmethod

class LanguageLabSessionBase(ABC):
    """
    Clase base abstracta para sesiones de laboratorio de idiomas.
    """
    @abstractmethod
    def get_lab_info(self):
        pass

class LanguageLabSession(LanguageLabSessionBase):
    """
    Representa una sesión concreta de laboratorio de idiomas.
    """
    def __init__(self, topic: str, duration: int):
        self.topic = topic
        self.duration = duration  # duración en minutos

    def get_lab_info(self):
        return f"Tema: {self.topic}, Duración: {self.duration} minutos"