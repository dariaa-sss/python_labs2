from model import BankAccount, CreditAccount, SaveAccount


class BankAccountCollection:
    def __init__(self):
        self._items = []

    def add(self, account):
        if not isinstance(account, BankAccount):
            raise TypeError("Неверный объект")
        for existing in self._items:
            if existing._number == account._number:
                raise ValueError(f"Аккаунт с таким номером уже добавлен")
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

    def filter_by_type(self, class_type):
        result = BankAccountCollection()
        for acc in self._items:
            if isinstance(acc, class_type):
                result.add(acc)
        return result

    def get_credit_accounts(self):
        return self.filter_by_type(CreditAccount)

    def get_savings_accounts(self):
        return self.filter_by_type(SaveAccount)
