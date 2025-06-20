from abc import ABC, abstractmethod

class LoginSystemBase(ABC):
    """
    Clase base abstracta para sistemas de login.
    """
    @abstractmethod
    def add_account(self, account):
        pass

    @abstractmethod
    def login(self, username: str, password: str) -> bool:
        pass

class LoginSystem(LoginSystemBase):
    """
    Gestiona el login y autenticación de usuarios.
    """
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.username] = account

    def login(self, username: str, password: str) -> bool:
        account = self.accounts.get(username)
        if account:
            return account.check_password(password)
        return False