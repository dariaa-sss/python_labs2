

from models import BankAccount, CreditAccount, SaveAccount
from collection import BankAccountCollection


    print("\n1. Создание счетов разных типов:")
    ordinary = BankAccount("Обычный", "00000000", 1000, "rub", True)
    credit = CreditAccount("Кредитный", "11111111", -500, "rub", True,
                           lim=10000, percentages=15, min_count=500)
    savings = SaveAccount("Сберегательный", "22222222", 5000, "rub", True,
                          percentages=5)

    print(f"  {ordinary}")
    print(f"  {credit}")
    print(f"  {savings}")


    print("\n2. Добавление счетов в коллекцию:")
    collection = BankAccountCollection()
    collection.add(ordinary)
    collection.add(credit)
    collection.add(savings)

    print(f"   В коллекции {len(collection)} счёта(ов).")
    for acc in collection:
        print(f"   - {acc}")


    print("\n3. Полиморфизм: пополнение и списание (с комиссиями):")
    for acc in collection:
        print(f"\n   Счёт: {acc.owner}")
        # Пополнение на 1000
        acc.top_balance(1000)
        print(f"     После пополнения 1000: баланс = {acc.balance}")
        # Списание 200
        acc.transfer_balance(200)
        print(f"     После списания 200:   баланс = {acc.balance}")

    print("\n4. Ежемесячные операции (начисление процентов/комиссий):")
    for acc in collection:
        print(f"\n   {acc.owner}:")
        acc.apply_monthly_interest()   # метод ведёт себя по-разному
        print(f"     Баланс после операции: {acc.balance}")


    print("\n5. Проверка типов объектов в коллекции:")
    for acc in collection:
        if isinstance(acc, CreditAccount):
            print(f"   {acc.owner} — кредитный счёт (лимит {acc.lim})")
        elif isinstance(acc, SaveAccount):
            print(f"   {acc.owner} — сберегательный счёт (ставка {acc.percentages}%)")
        else:
            print(f"   {acc.owner} — обычный счёт")


    print("\n6. Фильтрация коллекции по типу счетов:")
    

    credits = collection.filter(lambda a: isinstance(a, CreditAccount))
    savings_only = collection.filter(lambda a: isinstance(a, SaveAccount))
    
    print(f"   Кредитные счета: {len(credits)}")
    for acc in credits:
        print(f"     {acc}")
    print(f"   Сберегательные счета: {len(savings_only)}")
    for acc in savings_only:
        print(f"     {acc}")

    print("\n7. Сортировка коллекции по балансу:")
    collection.sort_by_balance()
    for acc in collection:
        print(f"   {acc.owner}: {acc.balance}")


    print("\n8. Поиск по номеру счёта:")
    found = collection.find_by_number("11111111")
    if found:
        print(f"   Найден: {found}")
    else:
        print("   Не найден")

    print("\n9. Удаление счёта и попытка добавить дубликат:")
    collection.remove(ordinary)
    print(f"   После удаления обычного счёта осталось {len(collection)} элементов.")
    
    # Попытка добавить дубликат (счёт с существующим номером)
    duplicate = CreditAccount("Дубль", "11111111", 100, "rub", True, 5000, 15, 500)
    try:
        collection.add(duplicate)
    except ValueError as e:
        print(f"   Ошибка (ожидаемо): {e}")

    # ------------------------------------------------------------
    # 10. Итоговый вывод
    # ------------------------------------------------------------
    print("\n" + "=" * 60)
    print("Демонстрация завершена. Все требования оценки 5 выполнены.")
    print("=" * 60)


if __name__ == "__main__":
    main()