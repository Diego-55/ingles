from abc import ABC, abstractmethod

class Assessment(ABC):
    """
    Clase base abstracta para evaluaciones.
    """
    @abstractmethod
    def grade(self):
        pass

class Homework(Assessment):
    """
    Representa una evaluación tipo tarea.
    """
    def __init__(self, completed: bool):
        self.completed = completed

    def grade(self):
        return 100 if self.completed else 0