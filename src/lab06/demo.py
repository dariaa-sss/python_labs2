
from lab06.base import BankAccount
from lab06.model import CreditAccount, SaveAccount
from lab06.container import Displayable, Scorable, TypedCollection, D, S

def main() -> None:

    print("\n1. БАЗОВАЯ РАБОТА С TYPEDCOLLECTION")
    accounts: TypedCollection[BankAccount] = TypedCollection()

    acc1 = BankAccount("Иван Петров", "12345678", 5000.0, "rub", True)
    acc2 = CreditAccount("Мария Смирнова", "23456789", 3000.0, "dollar", True, 10000.0, 12.0, 1000.0)
    acc3 = SaveAccount("Петр Сидоров", "34567890", 12000.0, "rub", True, 5.0)
    acc4 = BankAccount("Анна Козлова", "45678901", 800.0, "rub", False)

    accounts.add(acc1)
    accounts.add(acc2)
    accounts.add(acc3)
    accounts.add(acc4)

    print("Все добавленные счета:")
    for acc in accounts.get_all():
        print(f"  {acc.display()}")

    print(f"\nРазмер коллекции: {accounts.size()}")
    accounts.remove(acc1)
    print(f"После удаления первого счета: {accounts.size()}")

    print("\n2. МЕТОДЫ FIND, FILTER, MAP")
    found = accounts.find(lambda a: a.balance > 10000)
    print(f"Найден счёт с балансом > 10000: {found.display() if found else 'None'}")

    not_found = accounts.find(lambda a: a.balance > 50000)
    print(f"Поиск несуществующего: {not_found}")

    active_accs = accounts.filter(lambda a: a.is_active)
    print("\nАктивные счета:")
    for acc in active_accs:
        print(f"  {acc.display()}")

    owners = accounts.map(lambda a: a.owner)
    print(f"\nВладельцы: {owners}")

    balances = accounts.map(lambda a: a.balance)
    print(f"Балансы: {balances}")

    descriptions = accounts.map(lambda a: f"{a.owner} – {a.balance} {a.currency}")
    print("\nОписания счетов:")
    for desc in descriptions:
        print(f"  {desc}")

    print("\n3. ПРОТОКОЛЫ И ОГРАНИЧЕННЫЕ TYPEVAR")

    def print_all_displayable(collection: TypedCollection[D]) -> None:
        for item in collection.get_all():
            print(item.display())

    def print_all_scores(collection: TypedCollection[S]) -> None:
        for item in collection.get_all():
            print(f"{item.display()} -> score = {item.score():.2f}")

    displayable_coll: TypedCollection[Displayable] = TypedCollection()
    displayable_coll.add(BankAccount("Алексей Орлов", "11111111", 7000, "rub", True))
    displayable_coll.add(CreditAccount("Елена Ветрова", "22222222", 1500, "dollar", True, 5000, 18, 500))
    displayable_coll.add(SaveAccount("Ольга Новикова", "33333333", 25000, "rub", True, 3))

    print("\nКоллекция Displayable объектов (разные типы)")
    print_all_displayable(displayable_coll)

    scorable_coll: TypedCollection[Scorable] = TypedCollection()
    scorable_coll.add(BankAccount("Денис Зайцев", "44444444", 500, "rub", True))
    scorable_coll.add(CreditAccount("Светлана Морозова", "55555555", 2000, "dollar", True, 10000, 20, 1000))
    scorable_coll.add(SaveAccount("Татьяна Лебедева", "66666666", 30000, "rub", True, 4.5))

    print("\nКоллекция Scorable объектов (разные типы)")
    print_all_scores(scorable_coll)

    print("\nСтруктурная типизация (без наследования от протоколов)")
    some_objects: list[Displayable] = [
        BankAccount("Виктор Павлов", "77777777", 10000, "rub", True),
        CreditAccount("Наталья Романова", "88888888", 5000, "dollar", True, 8000, 15, 800)
    ]
    for obj in some_objects:
        print(obj.display())



if __name__ == "__main__":
    main()