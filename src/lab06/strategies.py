'''
функции для сортировки: имя, баланс, комбинированный

2 функции-фильтра: is_active, balance>=1000000

1 фабрика функций: функция, которая возвращает другую функцию(make_min_balance_filter(min_balance))

1 класс-стратегия (callable) – FeeStrategy с методом __call__'''

def by_balance(account):
    return account.balance

def by_owner(account):
    return account.owner

def key_owner_balance(account):
    return account.owner, account.balance

def filter_active(account):
    return account.is_active
    
def filter_vip_balance(account):
    return account.balance >= 1000000

def make_min_balance_filter(min_balance):
    def predicate(account):
        return account.balance >= min_balance
    return predicate

class FeeStrategy:
    def __init__(self, percent):
        self.percent = percent
    def __call__(self, account):
        account.balance -= account.balance * self.percent / 100
        return account