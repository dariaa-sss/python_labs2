from typing import List
from lab06.base import BankAccount
from lab05.collection import BankAccountCollection
from exceptions import AccountNotFoundError, DuplicateAccountError
import storage


class App:
    def __init__(self) -> None:
        self._collection: BankAccountCollection = BankAccountCollection()
        self._path: str = "accounts.json"

    def load_data(self) -> None:
        accounts = storage.load(self._path)
        for acc in accounts:
            self._collection.add(acc)

    def save_data(self) -> None:
        import os
        print(f"Сохраняю в: {os.path.abspath(self._path)}")
        storage.save(self._collection.get_all(), self._path)

    def add_account(self, account: BankAccount) -> None:
        print(f"Добавляю: {account}, тип: {type(account)}")
        print(f"Размер до: {len(self._collection)}")
        existing = self._collection.find_by_number(account._number)
        if existing is not None:
            raise DuplicateAccountError(
                f"Счёт с номером {account._number} уже существует"
            )
        self._collection.add(account)
        print(f"Размер после: {len(self._collection)}")

    def get_all(self) -> List[BankAccount]:
        return self._collection.get_all()

    def find_by_number(self, number: str) -> BankAccount:
        account = self._collection.find_by_number(number)
        if account is None:
            raise AccountNotFoundError(f"Счёт {number} не найден")
        return account

    def delete_account(self, number: str) -> None:
        account = self.find_by_number(number)  # сам бросит исключение если не найден
        self._collection.remove(account)

    def top_up(self, number: str, amount: float) -> str:
        account = self.find_by_number(number)
        result = account.top_balance(amount)
        return result

    def filter_by_balance(self, min_b: float, max_b: float) -> List[BankAccount]:
        return self._collection.filter(
            lambda acc: min_b <= acc.balance <= max_b
        )

    def filter_active(self) -> List[BankAccount]:
        return self._collection.filter(lambda acc: acc.is_active)

    def sort_by(self, strategy: str) -> None:
        if strategy == "balance":
            self._collection.sort_by_balance()
        elif strategy == "owner":
            self._collection.sort_by_owner()

    def apply_interest(self) -> None:
        for acc in self._collection:
            acc.apply_monthly_interest()