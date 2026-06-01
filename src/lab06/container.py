from typing import TypeVar, Generic, List, Callable, Optional, Protocol, Any
from lab06.interfaces import Printable, Comparable

class Displayable(Protocol):
    def display(self) -> str:
        pass

class Scorable(Protocol):
    def score(self) -> float:
        pass

T = TypeVar('T')
R = TypeVar('R')
D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)

class TypedCollection(Generic[T]):

    def __init__(self) -> None:
        self._items: List[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def remove(self, item: T) -> None:
        self._items.remove(item)

    def remove_at(self, index: int) -> T:
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс уходит за границы")
        return self._items.pop(index)

    def get_all(self) -> List[T]:
        return list(self._items)

    def find_by_owner(self, owner_name: str) -> List[T]:
        result = []
        for item in self._items:
            if hasattr(item, 'owner') and item.owner == owner_name:
                result.append(item)
        return result

    def find_by_number(self, number: str) -> Optional[T]:
        for item in self._items:
            if hasattr(item, '_number') and item._number == number:
                return item
        return None

    def size(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index: int) -> T:
        return self._items[index]

    def sort(self, key: Optional[Callable[[T], Any]] = None, reverse: bool = False) -> None:
        self._items.sort(key=key, reverse=reverse)

    def sort_by_balance(self, reverse: bool = False) -> None:
        self.sort(key=lambda acc: acc.balance, reverse=reverse)

    def sort_by_owner(self, reverse: bool = False) -> None:
        self.sort(key=lambda acc: acc.owner, reverse=reverse)

    def sort_by(self, key_func: Callable[[T], Any], reverse: bool = False) -> "TypedCollection[T]":
        self._items.sort(key=key_func, reverse=reverse)
        return self

    def get_active(self) -> "TypedCollection[T]":
        new_coll = TypedCollection[T]()
        for item in self._items:
            if hasattr(item, 'is_active') and item.is_active:
                new_coll.add(item)
        return new_coll

    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        return [item for item in self._items if predicate(item)]

    def filter_by(self, predicate: Callable[[T], bool]) -> "TypedCollection[T]":
        new_coll = TypedCollection[T]()
        for item in self._items:
            if predicate(item):
                new_coll.add(item)
        return new_coll

    def apply(self, func: Callable[[T], Any]) -> "TypedCollection[T]":
        for item in self._items:
            func(item)
        return self

    def get_printable(self) -> List[T]:
        return [item for item in self._items if isinstance(item, Printable)]

    def get_comparable(self) -> List[T]:
        return [item for item in self._items if isinstance(item, Comparable)]

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None

    def map(self, transform: Callable[[T], R]) -> List[R]:
        return [transform(item) for item in self._items]