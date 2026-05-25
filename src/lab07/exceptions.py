class AccountNotFoundError(Exception):
    '''аккаунт не найден'''
    pass


class DuplicateAccountError(Exception):
    '''такой аккаунт уже существует'''
    pass


class InactiveAccountError(Exception):
    '''операция для неактивного аккаунта'''
    pass