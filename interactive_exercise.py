from abc import ABC, abstractmethod

class InteractiveExerciseBase(ABC):
    """
    Clase base abstracta para ejercicios interactivos.
    """
    @abstractmethod
    def get_description(self):
        pass

class InteractiveExercise(InteractiveExerciseBase):
    """
    Representa un ejercicio interactivo concreto.
    """
    def __init__(self, description: str):
        self.description = description

    def get_description(self):
        return self.description