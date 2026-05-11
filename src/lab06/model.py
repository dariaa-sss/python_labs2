# credit_account.py (ваш файл)
from base import BankAccount
from validators import val_owner, val_number, val_balance, val_currency, val_active

class CreditAccount(BankAccount):
    def __init__(self, owner: str, number: str, balance: float, currency: str,
                 is_active: bool, lim: float, percentages: float, min_count: float) -> None:
        super().__init__(owner, number, balance, currency, is_active)
        self.lim: float = lim
        self.percentages: float = percentages
        self.min_count: float = min_count

    def __str__(self) -> str:
        return super().__str__() + f", ставка={self.percentages}%"

    def top_balance(self, amount: float): #-> Optional[str]:
        self.balance += amount - amount * 0.15
        if val_balance(self.balance):
            return f"Баланс после пополнения: {self.balance}"
        return None

    def transfer_balance(self, amount: float): #-> Optional[str]:
        self.balance -= amount + amount * 0.15
        if val_balance(self.balance):
            return f"Баланс после перевода: {self.balance}"
        return None

    def apply_monthly_interest(self) -> None:
        if self.balance < 0:
            interest = abs(self.balance) * self.percentages / 100
            self.balance -= interest
            print(f"Начислены проценты по кредиту, баланс = {self.balance}")

    def to_string(self) -> str:
        return str(self)

    def display(self) -> str:
        return f"CreditAccount: {self.owner}, баланс: {self.balance} {self.currency}, лимит: {self.lim}"

    def score(self) -> float:
        base = min(5.0, max(0.0, self.balance / 1000))
        if self.balance < 0:
            base *= 0.5
        return base


class SaveAccount(BankAccount):
    def __init__(self, owner: str, number: str, balance: float, currency: str,
                 is_active: bool, percentages: float) -> None:
        super().__init__(owner, number, balance, currency, is_active)
        self.percentages: float = percentages

    def __str__(self) -> str:
        return super().__str__() + f", ставка={self.percentages}%"

    def top_balance(self, amount: float):# -> Optional[str]:
        self.balance += amount - amount * 0.05
        if val_balance(self.balance):
            return f"Баланс после пополнения: {self.balance}"
        return None

    def transfer_balance(self, amount: float):# -> Optional[str]:
        self.balance -= amount + amount * 0.05
        if val_balance(self.balance):
            return f"Баланс после перевода: {self.balance}"
        return None

    def apply_monthly_interest(self) -> None:
        self.balance += self.balance * self.percentages / 100
        print(f"Начислены проценты, баланс = {self.balance}")

    def to_string(self) -> str:
        return str(self)

    # ДЛЯ ПРОТОКОЛОВ:
    def display(self) -> str:
        return f"SaveAccount: {self.owner}, баланс: {self.balance} {self.currency}, ставка: {self.percentages}%"

    def score(self) -> float:
        return min(5.0, self.balance / 800)