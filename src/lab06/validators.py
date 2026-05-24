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


def val_activ(active: bool, new_status: bool):
    if active == new_status:
        return f"такой статус уже установлен"
