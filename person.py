from abc import ABC, abstractmethod

class Person(ABC):
    """
    Abstract base class for a person in the academy.
    """
    def __init__(self, name: str, email: str):
        self._name = name
        self._email = email

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @abstractmethod
    def get_role(self) -> str:
        pass
