from typing import Optional
from app import App
from lab06.base import BankAccount
from lab06.model import CreditAccount, SaveAccount
from exceptions import AccountNotFoundError, DuplicateAccountError


class CLI:
    '''консольное меню и обработка ввода'''
    def __init__(self) -> None:
        self._app: App = App()

    def run(self) -> None:
        '''
        главный цикл приложения,загружает данные, 
        отображает меню и перенаправляет команды пользователя,
        при выходе из цикла сохраняет данные
        '''
        self._app.load_data()
        print("Данные загружены.")

        while True:
            self._print_menu()
            choice = self._get_int("Выберите пункт: ")

            if choice == 0:
                self._app.save_data()
                print("Данные сохранены. До свидания!")
                break
            elif choice == 1:
                self._add_account()
            elif choice == 2:
                self._show_all()
            elif choice == 3:
                self._find_account()
            elif choice == 4:
                self._delete_account()
            elif choice == 5:
                self._top_up()
            elif choice == 6:
                self._filter_by_balance()
            elif choice == 7:
                self._sort_accounts()
            elif choice == 8:
                self._apply_interest()
            else:
                print("Нет такого пункта. Попробуйте снова.")

    def _print_menu(self) -> None:
        '''выводит список доступных действий в консоль'''
        print("  Главное меню")
        print("\n")
        print("1. Добавить счёт")
        print("2. Показать все счета")
        print("3. Найти счёт по номеру")
        print("4. Удалить счёт")
        print("5. Пополнить баланс")
        print("6. Фильтр по балансу")
        print("7. Сортировка")
        print("8. Начислить проценты")
        print("0. Выход")
        print("\n")

    def _get_int(self, prompt: str) -> int:
        '''запрашивает у пользователя целое число, проверяет на корректность,
        повторяет запрос при вводе некорректных данных'''
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Ошибка: введите целое число.")

    def _get_float(self, prompt: str) -> float:
        '''запрашивает у пользователя нецелое число, проверяет на корректность,
        повторяет запрос при вводе некорректных данных'''
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Ошибка: введите число.")

    def _confirm(self, message: str) -> bool:
        '''проверяет, точно ли пользователь уверен в своем выборе'''
        ans = input(f"{message} (y/n): ").strip().lower()
        return ans == "y"

    def _print_table(self, accounts: list) -> None:
        '''форматирует и выводит список счетов в виде таблицы'''
        if not accounts:
            print("Список пуст.")
            return

        print(f"\n{'Тип':<15} {'Владелец':<15} {'Номер':<12} "
              f"{'Баланс':>12} {'Валюта':<8} {'Статус'}")
        print("-" * 70)

        for acc in accounts:
            ttype = type(acc).__name__
            status = "активен" if acc.is_active else "закрыт"
            print(
                f"{ttype:<15} {acc.owner:<15} {acc._number:<12} "
                f"{acc.balance:>12.2f} {acc.currency:<8} {status}"
            )

    def _add_account(self) -> None:
        print("\nТип счёта:")
        print("1. BankAccount")
        print("2. CreditAccount")
        print("3. SaveAccount")
        type_choice = self._get_int("Выберите тип: ")
        owner = input("Владелец: ").strip()
        number = input("Номер (8–16 цифр): ").strip()
        balance = self._get_float("Баланс: ")
        currency = input("Валюта (rub/dollar): ").strip()
        is_active_str = input("Активен? (y/n): ").strip().lower()
        is_active = is_active_str == "y"

        try:
            if type_choice == 1:
                account = BankAccount(owner, number, balance, currency, is_active)

            elif type_choice == 2:
                lim = self._get_float("Кредитный лимит: ")
                percentages = self._get_float("Ставка (%): ")
                min_count = self._get_float("Минимальный платёж: ")
                account = CreditAccount(
                    owner, number, balance, currency, is_active,
                    lim, percentages, min_count
                )

            elif type_choice == 3:
                percentages = self._get_float("Ставка (%): ")
                account = SaveAccount(
                    owner, number, balance, currency, is_active, percentages
                )

            else:
                print("Неверный тип.")
                return

            self._app.add_account(account)
            print("Счёт добавлен.")

        except DuplicateAccountError as e:
            print(f"Ошибка: {e}")
        except (ValueError, TypeError) as e:
            print(f"Ошибка данных: {e}")

    def _show_all(self) -> None:
        accounts = self._app.get_all()
        self._print_table(accounts)

    def _find_account(self) -> None:
        number = input("Номер счёта: ").strip()
        try:
            account = self._app.find_by_number(number)
            self._print_table([account])
        except AccountNotFoundError as e:
            print(f"Ошибка: {e}")

    def _delete_account(self) -> None:
        number = input("Номер счёта для удаления: ").strip()
        if self._confirm(f"Удалить счёт {number}?"):
            try:
                self._app.delete_account(number)
                print("Счёт удалён.")
            except AccountNotFoundError as e:
                print(f"Ошибка: {e}")

    def _top_up(self) -> None:
        number = input("Номер счёта: ").strip()
        amount = self._get_float("Сумма пополнения: ")
        try:
            result = self._app.top_up(number, amount)
            print(f"✓ {result}")
        except AccountNotFoundError as e:
            print(f"Ошибка: {e}")
        except ValueError as e:
            print(f"Ошибка: {e}")

    def _filter_by_balance(self) -> None:
        min_b = self._get_float("Минимальный баланс: ")
        max_b = self._get_float("Максимальный баланс: ")
        accounts = self._app.filter_by_balance(min_b, max_b)
        self._print_table(accounts)

    def _sort_accounts(self) -> None:
        print("\nСортировать по:")
        print("1. Балансу")
        print("2. Владельцу")
        choice = self._get_int("Выберите: ")

        if choice == 1:
            self._app.sort_by("balance")
        elif choice == 2:
            self._app.sort_by("owner")
        else:
            print("Неверный выбор")
            return

        print("Коллекция отсортирована")
        self._show_all()

    def _apply_interest(self) -> None:
        self._app.apply_interest()
        print("Проценты начислены")