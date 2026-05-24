import json
from lab06.base import BankAccount
from lab06.model import CreditAccount, SaveAccount


def _account_to_dict(account: BankAccount) -> dict:
    data = {
        "type": type(account).__name__,
        "owner": account.owner,
        "number": account._number,
        "balance": account.balance,
        "currency": account.currency,
        "is_active": account.is_active,
    }

    if isinstance(account, CreditAccount):
        data["lim"] = account.lim
        data["percentages"] = account.percentages
        data["min_count"] = account.min_count
    elif isinstance(account, SaveAccount):
        data["percentages"] = account.percentages
    return data


def _dict_to_account(data: dict) -> BankAccount:
    t = data["type"]  
    if t == "CreditAccount":
        return CreditAccount(
            data["owner"],
            data["number"],
            data["balance"],
            data["currency"],
            data["is_active"],
            data["lim"],
            data["percentages"],
            data["min_count"],
        )

    elif t == "SaveAccount":
        return SaveAccount(
            data["owner"],
            data["number"],
            data["balance"],
            data["currency"],
            data["is_active"],
            data["percentages"],
        )

    else:  
        return BankAccount(
            data["owner"],
            data["number"],
            data["balance"],
            data["currency"],
            data["is_active"],
        )


def save(accounts: list, filepath: str) -> None:
    data = [_account_to_dict(acc) for acc in accounts]
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load(filepath: str) -> list:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [_dict_to_account(d) for d in data]
    except FileNotFoundError:
        return []