from model import BankAccount, CreditAccount, SaveAccount
from collection import BankAccountCollection


def main():

    ordinary = BankAccount("Обычный", "00000000", 1000, "rub", True)
    credit = CreditAccount("Кредитный", "11111111", 500, "rub", True,
                           lim=10000, percentages=15, min_count=500)
    savings = SaveAccount("Сберегательный", "22222222", 5000, "rub", True,
                          percentages=5)

    print("\n1. Создание счетов разных типов:")
    print(f"  {ordinary}")
    print(f"  {credit}")
    print(f"  {savings}")

    collection = BankAccountCollection()
    collection.add(ordinary)
    collection.add(credit)
    collection.add(savings)

    print("\n2. Коллекция после добавления:")
    print(f"   Всего счетов: {len(collection)}")
    for acc in collection:
        print(f"   - {acc}")

    print("\n3. Полиморфизм: пополнение и списание (с комиссиями):")
    for acc in collection:
        print(f"\n   Счёт: {acc.owner}")
        acc.top_balance(1000)
        print(f"     После пополнения 1000: баланс = {acc.balance}")
        acc.transfer_balance(200)
        print(f"     После списания 200:   баланс = {acc.balance}")

    print("\n4. Ежемесячные операции (apply_monthly_interest):")
    for acc in collection:
        print(f"\n   {acc.owner}:")
        acc.apply_monthly_interest()
        print(f"     Баланс после операции: {acc.balance}")

    print("\n5. Проверка типов через isinstance():")
    for acc in collection:
        if isinstance(acc, CreditAccount):
            print(f"   {acc.owner} — кредитный счёт (лимит {acc.lim})")
        elif isinstance(acc, SaveAccount):
            print(f"   {acc.owner} — сберегательный счёт (ставка {acc.percentages}%)")
        else:
            print(f"   {acc.owner} — обычный счёт")

    print("\n6. Фильтрация коллекции по типу:")
    credits = collection.filter(lambda a: isinstance(a, CreditAccount))
    savings_only = collection.filter(lambda a: isinstance(a, SaveAccount))

    print(f"   Кредитные счета: {len(credits)}")
    for acc in credits:
        print(f"     {acc}")
    print(f"   Сберегательные счета: {len(savings_only)}")
    for acc in savings_only:
        print(f"     {acc}")

    print("\n7. Сортировка по балансу:")
    collection.sort_by_balance()
    for acc in collection:
        print(f"   {acc.owner}: {acc.balance}")

    print("\n8. Поиск по номеру счёта:")
    found = collection.find_by_number("11111111")
    if found:
        print(f"   Найден: {found}")
    else:
        print("   Не найден")

    print("\n9. Удаление счёта и проверка дубликата:")
    collection.remove(ordinary)
    print(f"   После удаления обычного счёта осталось {len(collection)} элементов.")

    duplicate = CreditAccount("Дубль", "11111111", 100, "rub", True, 5000, 15, 500)
    try:
        collection.add(duplicate)
    except ValueError as e:
        print(f"   Ошибка (ожидаемо): {e}")



if __name__ == "__main__":
    main()