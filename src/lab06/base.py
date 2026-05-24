# base.py
from typing import Optional
from interfaces import Printable, Comparable
from validators import val_owner, val_number, val_balance, val_currency, val_active

CURRENCIES = ("rub", "dollar")

class BankAccount(Printable, Comparable):
    def __init__(self, owner: str, number: str, balance: float,
                 currency: str, is_active: bool) -> None:
        self.owner: str = val_owner(owner)
        self._number: str = val_number(number)
        self.balance: float = val_balance(balance)
        self._currency: str = val_currency(currency, CURRENCIES)
        self.is_active: bool = val_active(is_active)

    def __str__(self) -> str:
        return f"владелец счета {self.owner}, номер карты {self._number}"

    def __repr__(self) -> str:
        return f"owner={self.owner}, number={self._number}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self._number == other._number

    @property
    def currency(self) -> str:
        return self._currency

    @currency.setter
    def currency(self, val: str) -> None:
        if val not in CURRENCIES:
            raise ValueError("недопустимая валюта")
        if val == self._currency:
            raise ValueError("выберите другую валюту")
        self._currency = val

    def top_balance(self, amount: float) -> Optional[str]:
        self.balance += amount
        return f"Баланс после пополнения: {self.balance}"

    def transfer_balance(self, amount: float) -> Optional[str]:
        self.balance -= amount
        return f"Баланс после перевода: {self.balance}"

    def active(self, mood: bool) -> bool:
        self.is_active = mood
        return self.is_active

    def apply_monthly_interest(self) -> None:
        print("нет начисления процентов")

    def to_string(self) -> str:
        return str(self)

    def compare_to(self, other: object) -> int:
        if not isinstance(other, BankAccount):
            raise TypeError("Можно сравнивать только с BankAccount")
        if self.balance < other.balance:
            return -1
        if self.balance > other.balance:
            return 1
        return 0

    def display(self) -> str:
        return f"BankAccount: {self.owner}, баланс: {self.balance} {self.currency}"

    def score(self) -> float:
        return min(5.0, self.balance / 1000)