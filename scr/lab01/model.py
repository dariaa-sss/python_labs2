from validators import (
    val_owner,
    val_number,
    val_balance,
    val_currency,
    val_active,
)

currencies = ("rub", "dollar")


class BankAccount:

    def __init__(self, owner, number, balance, currency, is_active):
        self.owner = val_owner(owner)
        self._number = val_number(number)
        self.balance = val_balance(balance)
        self._currency = val_currency(currency, currencies)
        self.is_active = val_active(is_active)
    
    def __str__(self):
        return f'владелец счета {self.owner},номер карты {self._number}'

    def __repr__(self):
        return f'owner={self.owner}, number={self._number}'
    
    def __eq__(self, other):
        if not isinstance(other,BankAccount):
            return NotImplemented
        return self._number== other._number

         

    @property
    def currency(self):
        return self._curency 
    @currency.setter
    def currency(self, val: str):
        if val not in currencies:
            raise ValueError('недопустимая валюта')
        if val == self._currency:
            raise ValueError('выберите другую валюту')
        self._currency = val
    
    def top_balance(self,amount:float):
        self.balance+=amount
        return val_balance(self.balance) and f'(f"Баланс после пополнения: {self.balance}'
    
    def transfer_balance(self,amount:float):
        self.balance-=amount
        return val_balance(self.balance) and f"Баланс после перевода: {self.balance}"
    
    def active(self,mood:bool):
        self.is_active=mood
        return val_active(self.is_active)



user1=BankAccount('dima','12345678',100,'rub',True)
print(user1)
