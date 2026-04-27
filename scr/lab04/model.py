from interfaces import Printable, Comparable
from base import BankAccount
from validators import (
    val_owner,
    val_number,
    val_balance,
    val_currency,
    val_active,
)

currencies = ("rub", "dollar")


class CreditAccount(BankAccount,Printable, Comparable):
    def __init__(
        self, owner, number, balance, currency, is_active, lim, percentages, min_count
    ):
        super().__init__(owner, number, balance, currency, is_active)
        self.lim = lim
        self.percentages = percentages
        self.min_count = min_count

    def __str__(self):
        return super().__str__() + f", ставка={self.percentages}%"

    def top_balance(self, amount: float):
        self.balance += amount - amount * 0.15

        return (
            val_balance(self.balance) and f'(f"Баланс после пополнения: {self.balance}'
        )

    def transfer_balance(self, amount: float):
        self.balance -= amount + amount * 0.15
        return val_balance(self.balance) and f"Баланс после перевода: {self.balance}"

    def apply_monthly_interest(self):
        if self.balance < 0:
            interest = abs(self.balance) * self.percentages / 100
            self.balance -= interest
            print(f"Начислены проценты по кредиту, баланс = {self.balance}")
    
    def to_string(self):
        return str(self)


class SaveAccount(BankAccount,Printable, Comparable):
    def __init__(self, owner, number, balance, currency, is_active, percentages):
        super().__init__(owner, number, balance, currency, is_active)
        self.percentages = percentages

    def __str__(self):
        return super().__str__() + f", ставка={self.percentages}%"

    def top_balance(self, amount: float):
        self.balance += amount - amount * 0.05

        return (
            val_balance(self.balance) and f'(f"Баланс после пополнения: {self.balance}'
        )

    def transfer_balance(self, amount: float):
        self.balance -= amount + amount * 0.05
        return val_balance(self.balance) and f"Баланс после перевода: {self.balance}"

    def apply_monthly_interest(self):
        self.balance += self.balance * self.percentages / 100
        print(f"Начислены проценты, баланс = {self.balance}")

    def to_string(self):
        return str(self)