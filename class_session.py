from abc import ABC, abstractmethod

class ClassSessionBase(ABC):
    """
    Clase base abstracta para sesiones de clase.
    """
    @abstractmethod
    def get_info(self):
        pass

class ClassSession(ClassSessionBase):
    """
    Representa una sesión de clase en un curso.
    """
    def __init__(self, topic: str, schedule):
        self.topic = topic
        self.schedule = schedule

    def get_info(self):
        return f"Tema: {self.topic}, Horario: {self.schedule}"