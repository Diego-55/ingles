from abc import ABC, abstractmethod

class PersonBase(ABC):
    """
    Clase base abstracta para personas.
    """
    @abstractmethod
    def get_role(self) -> str:
        pass

class Teacher(PersonBase):
    """
    Representa a un profesor en la academia de inglés.
    """
    def __init__(self, name: str, email: str, teacher_id: str):
        self.name = name
        self.email = email
        self._teacher_id = teacher_id

    @property
    def teacher_id(self):
        return self._teacher_id

    def get_role(self) -> str:
        return "Teacher"