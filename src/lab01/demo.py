from model import BankАccount


currencies = ("rub", "dollar")


def scenario_success():
    
    print("Сценарий 1: Успешные операции ")

    user = BankАccount("Dima", "12345678", 1000, "rub", True)
    print(user)

    user.top_balance(500)
    print(f"Баланс после пополнения: {user.balance}")

    user.transfer_balance(300)
    print(f"Баланс после перевода: {user.balance}")

    print()


def scenario_insufficient_funds():

    print("Сценарий 2: Недостаточно средств")

    user = BankАccount("Anna", "87654321", 200, "rub", True)

    try:
        user.transfer_balance(500)
    except ValueError as e:
        print(f"Ошибка: {e}")

    print()


def scenario_invalid_data():
 
    print("Сценарий 3: Ошибочные данные")

    try:
        user = BankАccount("", "12ab", -100, "euro", "yes")
    except (ValueError, TypeError) as e:
        print(f"Ошибка при создании счета: {e}")

    print()


if __name__ == "__main__":
    scenario_success()
    scenario_insufficient_funds()
    scenario_invalid_data()