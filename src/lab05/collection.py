from lab06.base import BankAccount
from lab06.model import SaveAccount, CreditAccount
from lab06.interfaces import Printable, Comparable

class BankAccountCollection:
    def __init__(self):
        self._items = []

    def add(self, account):
        if not isinstance(account, BankAccount):
            raise TypeError("Неверный объект")
        self._items.append(account)
        

    def remove(self, account):
        if not isinstance(account, BankAccount):
            raise TypeError("Неверный объект")
        try:
            self._items.remove(account)
        except ValueError:
            raise ValueError("Аккаунт не найден")

    def remove_at(self, index):
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс уходит за границы")
        return self._items.pop(index)

    def get_all(self):
        return self._items.copy()

    def find_by_owner(self, owner_name):
        result = []
        for acc in self._items:
            if acc.owner == owner_name:
                result.append(acc)
        return result

    def find_by_number(self, number):
        for acc in self._items:
            if acc._number == number:
                return acc
        return None

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self, key=None, reverse=False):
        self._items.sort(key=key, reverse=reverse)

    def sort_by_balance(self, reverse=False):
        self.sort(key=lambda acc: acc.balance, reverse=reverse)

    def sort_by_owner(self, reverse=False):
        self.sort(key=lambda acc: acc.owner, reverse=reverse)

    def get_active(self):
        new_collection = BankAccountCollection()
        for acc in self._items:
            if acc.is_active:
                new_collection.add(acc)
        return new_collection

    def filter(self, predicate):
        result = BankAccountCollection()
        for acc in self._items:
            if predicate(acc):
                result.add(acc)
        return result

    def get_printable(self):
        return [acc for acc in self._items if isinstance(acc, Printable)]

    def get_comparable(self):
        return [acc for acc in self._items if isinstance(acc, Comparable)]
    
    def sort_by(self, key_func, reverse=False):
        self._items.sort(key=key_func, reverse=reverse)
        return self

    def filter_by(self, predicate):
        new_coll = self.__class__()   
        for item in self._items:
            if predicate(item):
                new_coll.add(item)
        return new_coll

    def apply(self, func):
        for item in self._items:
            func(item)
        return self