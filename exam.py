from abc import ABC, abstractmethod

class Assessment(ABC):
    """
    Clase base abstracta para evaluaciones.
    """
    @abstractmethod
    def grade(self):
        pass

class Exam(Assessment):
    """
    Representa una evaluación tipo examen.
    """
    def __init__(self, score: float):
        self.score = score

    def grade(self):
        return self.score