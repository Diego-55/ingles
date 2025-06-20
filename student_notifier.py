from abc import ABC, abstractmethod
from student import Student

class Notifiable(ABC):
    """
    Clase base abstracta para objetos notificables.
    """
    @abstractmethod
    def notify(self, message: str):
        pass

class StudentNotifier(Student, Notifiable):
    def __init__(self, name, email, student_id):
        Student.__init__(self, name, email, student_id)

    def notify(self, message):
        return f"Notificación para {self.name} (estudiante): {message}"