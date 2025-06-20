from abc import ABC, abstractmethod

class ScheduleBase(ABC):
    """
    Clase base abstracta para horarios.
    """
    @abstractmethod
    def add_event(self, event):
        pass

    @abstractmethod
    def get_events(self):
        pass

class Schedule(ScheduleBase):
    """
    Representa un horario concreto.
    """
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def get_events(self):
        return self.events