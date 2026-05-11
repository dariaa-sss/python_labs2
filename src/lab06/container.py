"""
container.py
Generic-коллекция, протоколы и TypeVar с ограничениями.
"""

from typing import TypeVar, Generic, List, Callable, Optional, Protocol

# ========== Протоколы (структурные интерфейсы) ==========
class Displayable(Protocol):
    """Объект должен иметь метод display() -> str."""
    def display(self) -> str:
        ...

class Scorable(Protocol):
    """Объект должен иметь метод score() -> float."""
    def score(self) -> float:
        ...

# ========== TypeVar's ==========
T = TypeVar('T')          # для обычной коллекции
R = TypeVar('R')          # для map (тип результата)
D = TypeVar('D', bound=Displayable)   # ограничение: только Displayable
S = TypeVar('S', bound=Scorable)      # ограничение: только Scorable

# ========== Generic-коллекция ==========
class TypedCollection(Generic[T]):
    """
    Обобщённая коллекция, хранящая элементы типа T.
    Реализует интерфейс, аналогичный BankAccountCollection,
    но полностью типобезопасна.
    """

    def __init__(self) -> None:
        self._items: List[T] = []

    # --- Базовые методы (как в вашей BankAccountCollection, но без проверок типов) ---
    def add(self, item: T) -> None:
        """Добавляет элемент в коллекцию."""
        self._items.append(item)

    def remove(self, item: T) -> None:
        """Удаляет элемент (по равенству). Выбрасывает ValueError, если нет."""
        self._items.remove(item)

    def get_all(self) -> List[T]:
        """Возвращает копию списка элементов."""
        return list(self._items)

    def size(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return len(self._items) == 0

    # --- Методы для оценки 4 ---
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        """Возвращает первый элемент, удовлетворяющий условию, или None."""
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        """Возвращает список всех элементов, удовлетворяющих условию."""
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> List[R]:
        """Применяет функцию преобразования к каждому элементу, возвращает список результатов."""
        return [transform(item) for item in self._items]

    # --- Дополнительные удобные методы (необязательно, но полезно) ---
    def __len__(self) -> int:
        return len(self._items)

    def __getitem__(self, index: int) -> T:
        return self._items[index]

    def __iter__(self):
        return iter(self._items)