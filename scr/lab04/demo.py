
from base import BankAccount
from model import SaveAccount, CreditAccount
from collection import BankAccountCollection
from interfaces import Printable, Comparable

def print_all(items: list[Printable]) -> None:
    for item in items:
        print(item.to_string())

def find_min(comparable_list):
    if not comparable_list:
        return None
    min_item = comparable_list[0]
    for item in comparable_list[1:]:
        if item.compare_to(min_item) < 0:
            min_item = item
    return min_item

def main():
    cred1 = CreditAccount(
        owner="Иван Петров",
        number="12345678",
        balance=5000.0,
        currency="rub",
        is_active=True,
        lim=10000.0,
        percentages=15.0,
        min_count=1000.0
    )
    cred2 = CreditAccount(
        owner="Мария Сидорова",
        number="87654321",
        balance= 2000.0,
        currency="rub",
        is_active=True,
        lim=5000.0,
        percentages=18.0,
        min_count=500.0
    )
    save1 = SaveAccount(
        owner="Иван Петров",
        number="11112222",
        balance=100000.0,
        currency="dollar",
        is_active=True,
        percentages=5.0
    )
    save2 = SaveAccount(
        owner="Анна Козлова",
        number="33334444",
        balance=50000.0,
        currency="rub",
        is_active=False,
        percentages=4.5
    )

    collection = BankAccountCollection()
    for acc in (cred1, cred2, save1, save2):
        collection.add(acc)


    print("Использование интерфейса как типа (print_all)")
  
   
    all_accounts = collection.get_all()
    print_all(all_accounts)

    print("\nПроверка isinstance для объектов")
    for acc in all_accounts:
        print(acc.to_string())
        print(f"  Printable: {isinstance(acc, Printable)}")
        print(f"  Comparable: {isinstance(acc, Comparable)}")
        print()

    print("\nФильтрация коллекции по интерфейсам")
    printable_list = collection.get_printable()
    comparable_list = collection.get_comparable()
    print(f"Всего объектов в коллекции: {len(collection)}")
    print(f"Printable объектов: {len(printable_list)} (все, т.к. все счета реализуют Printable)")
    print(f"Comparable объектов: {len(comparable_list)} (все, т.к. все счета реализуют Comparable)")

    print("\nСравнение через Comparable (поиск минимального баланса)")
    min_acc = find_min(comparable_list)
    if min_acc:
        print(f"Счёт с минимальным балансом:")
        print(min_acc.to_string())
        print(f"Баланс: {min_acc.balance}")

    print("\nПолиморфизм без isinstance (вызов to_string напрямую)")
    for acc in collection.get_all():
        # Хороший стиль: просто вызываем метод, не проверяя тип
        print(acc.to_string())

if __name__ == "__main__":
    main()