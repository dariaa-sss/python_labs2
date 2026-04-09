# python_labs2


## Лабораторная работа №1  Bank Account
### Описание 
```Этот проект представляет собой систему управления банковскими счетами, разработанную в учебных целях. Система позволяет создавать банковские счета, управлять балансом, выполнять переводы между счетами и отслеживать статус активности счетов.```


### Структура
Проект состоит из трех основных файлов:

validators.py — модуль с функциями валидации

model.py — основной класс BankAccount

demo.py — демонстрационные сценарии

Детальное описание файлов
1. validators.py — Валидация данных
Этот файл содержит функции для проверки всех данных, которые попадают в систему. 

Функции валидации:

 - val_owner(owner) — проверяет имя владельца. 
    - Должно быть строкой
    - Не может быть пустым
    - Содержит только буквы, пробелы и дефисы

 - val_number(number) — проверяет номер счета

     - Должен быть строкой

     - Содержит от 8 до 16 цифр

     - Игнорирует пробелы и дефисы

 - val_balance(balance) — проверяет баланс

     - Должен быть числом

     - Не может быть отрицательным

     - Округляется до 2 знаков

 - val_amount(amount) — проверяет сумму операции

     - Должна быть числом

     - Должна быть больше 0

 - val_currency(currency, allowed) — проверяет валюту

     - Должна быть строкой

     - Должна быть в списке разрешенных валют

 - val_active(is_active) — проверяет статус активности

     - Должен быть булевым значением

 - val_status_change(current, new) — проверяет изменение статуса

     - Статус не может быть изменен на тот же самый

2. model.py — Класс BankAccount
Это сердце проекта. Здесь реализован сам банковский счет со всеми его методами.

Мой подход к разработке класса:

```Я использовала инкапсуляцию — все важные данные (номер счета, баланс) сделал приватными. Для доступа к балансу использовала @property, что позволяет контролировать изменения.```

## Атрибуты класса:

- owner — владелец счета

- _number — номер счета (приватный)

- _balance — баланс (приватный)

- currency — валюта

- is_active — статус активности

- _transaction_history — история операций


## Основные методы класса:

- top_up(amount) — пополнение счета

- withdraw(amount) — снятие средств

- transfer_to(target, amount) — перевод на другой счет

- set_active_status(status) — изменение статуса


```Я выбрала такую архитектуру, потому что хотел, чтобы класс был максимально приближен к реальному банковскому счету. Все операции проверяют:```

- Достаточно ли средств

- Активен ли счет

Корректна ли сумма

3. demo.py — Демонстрация работы
Этот файл показывает, как система работает в реальных сценариях. Я создал несколько сценариев, чтобы проверить разные ситуации.

## Сценарии:

### Успешные операции — демонстрация нормальной работы

![img01!](../../images/lab01/img01.png)


### Недостаточно средств — проверка обработки ошибок

![img02!](../../images/lab01/img02.png)


### Ошибочные данные — тестирование валидации при создании счета

![img03!](../../images/lab01/img03.png)


=======
## Лабораторная работа №1

### validators.py

```python
import re


def val_owner(owner: str) -> str:

    if not isinstance(owner, str):
        raise TypeError("Имя владельца должно быть строкой")

    owner = owner.strip()

    if not owner:
        raise ValueError("Имя владельца не может быть пустым")

    return owner


def val_number(number: str) -> str:

    if not isinstance(number, str):
        raise TypeError("Номер счета должен быть строкой")

    if not re.fullmatch(r"\d{8,16}", number):
        raise ValueError("Номер счета должен содержать от 8 до 16 цифр")

    return number


def val_balance(balance: float) -> float:
  
    if not isinstance(balance, (int, float)):
        raise TypeError("Баланс должен быть числом")

    if balance < 0:
        raise ValueError("Недостаточно средств на счете")

    return float(balance)


def val_amount(amount: float) -> float:
   
    if not isinstance(amount, (int, float)):
        raise TypeError("Сумма должна быть числом")

    if amount <= 0:
        raise ValueError("Сумма должна быть больше 0")

    return float(amount)


def val_currency(currency: str, allowed: tuple) -> str:
  
    if not isinstance(currency, str):
        raise TypeError("Валюта должна быть строкой")

    if currency not in allowed:
        raise ValueError(f"Доступные валюты: {', '.join(allowed)}")

    return currency


def val_active(is_active: bool) -> bool:
 
    if not isinstance(is_active, bool):
        raise TypeError("Статус активности должен быть True или False")

    return is_active
    

def val_activ(active:bool, new_status:bool):
    if active==new_status: return f'такой статус уже установлен'
    

    
```
### model.py

```python
from validators import (
    val_owner,
    val_number,
    val_balance,
    val_currency,
    val_active,
)

currencies = ("rub", "dollar")


class Bankaccount:

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
        if not isinstance(other,Bankaccount):
            return NotImplemented
        return self.owner== other.owner and self._number== other._number

         

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



user1=Bankaccount('dima','12345678',100,'rub',True)
print(user1)
```
### demo.py
```python
from model import Bankaccount


currencies = ("rub", "dollar")


def scenario_success():
    
    print("Сценарий 1: Успешные операции ")

    user = Bankaccount("Dima", "12345678", 1000, "rub", True)
    print(user)

    user.top_balance(500)
    print(f"Баланс после пополнения: {user.balance}")

    user.transfer_balance(300)
    print(f"Баланс после перевода: {user.balance}")

    print()


def scenario_insufficient_funds():

    print("Сценарий 2: Недостаточно средств")

    user = Bankaccount("Anna", "87654321", 200, "rub", True)

    try:
        user.transfer_balance(500)
    except ValueError as e:
        print(f"Ошибка: {e}")

    print()


def scenario_invalid_data():
 
    print("Сценарий 3: Ошибочные данные")

    try:
        user = Bankaccount("", "12ab", -100, "euro", "yes")
    except (ValueError, TypeError) as e:
        print(f"Ошибка при создании счета: {e}")

    print()


if __name__ == "__main__":
    scenario_success()
    scenario_insufficient_funds()
    scenario_invalid_data()
```
![img01!](./images/lab1/img01.png)

