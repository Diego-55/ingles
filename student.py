from abc import ABC, abstractmethod

class PersonBase(ABC):
    """
    Clase base abstracta para personas.
    """
    @abstractmethod
    def get_role(self) -> str:
        pass

class Student(PersonBase):
    """
    Representa a un estudiante en la academia de inglés.
    """
    def __init__(self, name: str, email: str, student_id: str):
        self.name = name
        self.email = email
        self._student_id = student_id

    @property
    def student_id(self):
        return self._student_id

    def get_role(self) -> str:
        return "Student"