from base import BankAccount
from model import CreditAccount, SaveAccount
from collection import BankAccountCollection
from strategies import (by_balance, by_owner, key_owner_balance, 
                        filter_active, filter_vip_balance, 
                        make_min_balance_filter, FeeStrategy)

def print_collection(title, coll):
    print(f"\n{title}:")
    for acc in coll.get_all():
        print(f"  {acc}")

def main():
    cred1 = CreditAccount("Иван Петров", "12345678", 5000.0, "rub", True, 10000.0, 15.0, 1000.0)
    cred2 = CreditAccount("Мария Сидорова", "87654321", 2000.0, "rub", True, 5000.0, 18.0, 500.0)
    save1 = SaveAccount("Иван Петров", "11112222", 100000.0, "dollar", True, 5.0)
    save2 = SaveAccount("Анна Козлова", "33334444", 50000.0, "rub", False, 4.5)
    save3 = SaveAccount("Петр Смирнов", "55556666", 2000000.0, "rub", True, 3.0)

    col = BankAccountCollection()
    for acc in (cred1, cred2, save1, save2, save3):
        col.add(acc)

    print("Сценарий 1: Цепочка filter -> sort -> apply")
    print_collection("Исходная коллекция", col)

    filtered = col.filter_by(filter_active)
    print_collection("После filter_by (только активные)", filtered)

    filtered.sort_by(by_balance, reverse=True)
    print_collection("После sort_by (по убыванию баланса)", filtered)

    fee = FeeStrategy(1.0)
    filtered.apply(fee)
    print_collection("После apply (комиссия 1%)", filtered)

    print("\n")
    print("Сценарий 2: Замена стратегии сортировки")
    col_copy = BankAccountCollection()
    for acc in col.get_all():
        col_copy.add(acc)

    print_collection("Сортировка по владельцу (by_owner)", col_copy.sort_by(by_owner))
    col_copy = BankAccountCollection()
    for acc in col.get_all():
        col_copy.add(acc)
    print_collection("Сортировка по балансу (by_balance)", col_copy.sort_by(by_balance))

    print("\n")
    print("Сценарий 3: Callable-стратегия (FeeStrategy) и lambda")
    test_col = BankAccountCollection()
    test_col.add(cred1)
    test_col.add(save1)

    print("До применения комиссии:")
    for acc in test_col.get_all():
        print(f"  {acc}")

    high_fee = FeeStrategy(5.0)
    test_col.apply(high_fee)
    print("\nПосле применения комиссии 5% через callable-объект:")
    for acc in test_col.get_all():
        print(f"  {acc}")

    print("\nИспользование lambda для сортировки по убыванию баланса:")
    sorted_lambda = sorted(test_col.get_all(), key=lambda a: a.balance, reverse=True)
    for acc in sorted_lambda:
        print(f"  {acc}")

    print("\n")
    print("map и filter")
    owners = list(map(lambda acc: acc.owner, col.get_all()))
    print("Владельцы всех счетов (map):", owners)

    vip = list(filter(filter_vip_balance, col.get_all()))
    print(f"VIP счета (баланс >= 1 000 000): {len(vip)}")
    for acc in vip:
        print(f"  {acc}")

    min_balance_filter = make_min_balance_filter(100000)
    rich = col.filter_by(min_balance_filter)
    print_collection("Счета с балансом >= 100 000 (фабрика фильтров)", rich)

if __name__ == "__main__":
    main()