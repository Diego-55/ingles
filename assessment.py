from abc import ABC, abstractmethod

class Assessment(ABC):
    """
    Clase base abstracta para evaluaciones.
    """
    @abstractmethod
    def grade(self):
        pass

class Exam(Assessment):
    def __init__(self, score):
        self.score = score

    def grade(self):
        if self.score >= 60:
            return "Aprobado"
        else:
            return "Reprobado"

class Homework(Assessment):
    def __init__(self, completed):
        self.completed = completed

    def grade(self):
        return "Completado" if self.completed else "Pendiente"