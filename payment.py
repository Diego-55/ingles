from abc import ABC, abstractmethod

class PaymentBase(ABC):
    """
    Clase base abstracta para pagos.
    """
    @abstractmethod
    def pay(self, amount: float):
        pass

    @abstractmethod
    def is_paid(self) -> bool:
        pass

class Payment(PaymentBase):
    """
    Representa un pago para un curso.
    """
    def __init__(self, amount: float, paid: bool = False):
        self.amount = amount
        self.paid = paid

    def pay(self, amount: float):
        if amount >= self.amount:
            self.paid = True

    def is_paid(self) -> bool:
        return self.paid