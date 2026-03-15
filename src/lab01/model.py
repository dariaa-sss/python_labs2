from validators import (
    val_owner,
    val_number,
    val_balance,
    val_currency,
    val_active,
)

currencies = ("rub", "dollar")


class BankАccount:

    def __init__(self, owner, number, balance, currency, is_active):
        self.owner = val_owner(owner)
        self._number = val_number(number)
        self._balance = val_balance(balance)
        self.currency = val_currency(currency, currencies)
        self.is_active = val_active(is_active)
    
    def __str__(self):
        return f'владелец счета {self.owner},номер карты {self._number}'

    def __repr__(self):
        return f'owner={self.owner}, number={self._number}'
    
    def __eq__(self, other):
        if not isinstance(other,BankАccount):
            return NotImplemented
        return self.owner== other.owner and self._number== other._number

         

    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, balance: str):
        if not isinstance(balance, (int, float)):
            raise TypeError("Баланс должен быть числом")

        if balance < 0:
            raise ValueError("Недостаточно средств на счете")

        self._balance = float(balance)
    
    def top_balance(self,amount:float):
        self.balance+=amount
        return val_balance(self.balance) and f'(f"Баланс после пополнения: {self.balance}'
    
    def transfer_balance(self,amount:float):
        self.balance-=amount
        return val_balance(self.balance) and f"Баланс после перевода: {self.balance}"
    
    def active(self,mood:bool):
        self.is_active=mood
        return val_active(self.is_active)


