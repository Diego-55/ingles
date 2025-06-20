from abc import ABC, abstractmethod

class AttendanceBase(ABC):
    """
    Clase base abstracta para gestionar asistencia.
    """
    @abstractmethod
    def mark(self, student, present: bool):
        pass

    @abstractmethod
    def get_attendance(self, student):
        pass

class Attendance(AttendanceBase):
    """
    Implementación concreta de AttendanceBase.
    """
    def __init__(self):
        self.records = {}

    def mark(self, student, present: bool):
        self.records[student] = present

    def get_attendance(self, student):
        return self.records.get(student, None)