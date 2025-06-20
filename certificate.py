from abc import ABC, abstractmethod

class CertificateBase(ABC):
    """
    Clase base abstracta para certificados.
    """
    @abstractmethod
    def get_certificate_info(self):
        pass

class Certificate(CertificateBase):
    """
    Representa un certificado para un estudiante y un curso.
    """
    def __init__(self, student, course):
        self.student = student
        self.course = course

    def get_certificate_info(self):
        return f"Certificado para {self.student} en el curso {self.course}"