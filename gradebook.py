from abc import ABC, abstractmethod

class GradebookBase(ABC):
    """
    Clase base abstracta para registros de calificaciones.
    """
    @abstractmethod
    def add_grade(self, student, grade):
        pass

    @abstractmethod
    def get_grade(self, student):
        pass

class Gradebook(GradebookBase):
    """
    Almacena calificaciones de estudiantes.
    """
    def __init__(self):
        self.grades = {}

    def add_grade(self, student, grade):
        self.grades[student] = grade

    def get_grade(self, student):
        return self.grades.get(student, None)