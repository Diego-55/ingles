from abc import ABC, abstractmethod

class StudentRankingBase(ABC):
    """
    Clase base abstracta para ranking de estudiantes.
    """
    @abstractmethod
    def get_top_students(self, n=3):
        pass

class StudentRanking(StudentRankingBase):
    """
    Ranks students by score.
    """
    def __init__(self, students):
        self.students = students

    def get_top_students(self, n=3):
        return sorted(self.students, key=lambda s: getattr(s, 'score', 0), reverse=True)[:n]