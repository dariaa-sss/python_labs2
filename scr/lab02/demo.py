from model import BankAccount
from collection import BankAccountCollection


def main():

    print("Создание счетов")
    acc1 = BankAccount("Dima", "11111111", 1000, "rub", True)
    acc2 = BankAccount("Anna", "22222222", 500, "rub", True)
    acc3 = BankAccount("Dima", "33333333", 2000, "dollar", False)
    acc4 = BankAccount("Olga", "44444444", 300, "rub", True)

    print("\nСоздание коллекции и добавление счетов")
    collection = BankAccountCollection()
    collection.add(acc1)
    collection.add(acc2)
    collection.add(acc3)
    collection.add(acc4)

    print(f"   В коллекции {len(collection)} элемента(ов).")
    print("   Содержимое:")
    for acc in collection:
        print(f"      {acc}")

    print("\nПоиск по атрибутам")
    found = collection.find_by_number("22222222")
    print(f"   Поиск по номеру 22222222: {found}")

    found_owners = collection.find_by_owner("Dima")
    print(f"   Счета владельца Dima: {len(found_owners)} шт.")
    for acc in found_owners:
        print(f"      {acc}")

    print("\nУдаление")
    collection.remove(acc2)
    print(f"   После удаления acc2: {len(collection)} элемента(ов).")
    collection.remove_at(0)
    print(f"   После удаления по индексу 0: {len(collection)} элемента(ов).")
    for acc in collection:
        print(f"      {acc}")

    print("\nСортировка по балансу (по возрастанию)")
    collection.sort_by_balance()
    for acc in collection:
        print(f"      {acc.owner}: {acc.balance} {acc.currency}")

    print("\nСортировка по владельцу (по убыванию)")
    collection.sort_by_owner(reverse=True)
    for acc in collection:
        print(f"      {acc.owner}: {acc.balance}")

    print("\nФильтрация (только активные счета)")
    active_collection = collection.get_active()
    print(f"   Активных счетов: {len(active_collection)}")
    for acc in active_collection:
        print(f"      {acc.owner} (active={acc.is_active})")

    print("\nФильтрация (баланс > 500)")
    high_balance = collection.filter(lambda a: a.balance > 500)
    print(f"   Счетов с балансом > 500: {len(high_balance)}")
    for acc in high_balance:
        print(f"      {acc.owner}: {acc.balance}")

    print("\nПопытка добавить дубликат (счет с уже существующим номером)")
    duplicate = BankAccount("Duplicate", "33333333", 999, "rub", True)
    try:
        collection.add(duplicate)
    except ValueError as e:
        print(f"   Ошибка (ожидаемо): {e}")

    print("\nДоступ по индексам (__getitem__)...")
    if len(collection) > 0:
        print(f"   Первый элемент: {collection[0]}")
        print(f"   Последний элемент: {collection[-1]}")

    print("\nИтерация по коллекции (for acc in collection):")
    for acc in collection:
        print(f"      {acc}")


if __name__ == "__main__":
    main()
