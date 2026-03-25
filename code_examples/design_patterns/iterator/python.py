from abc import ABC, abstractmethod
from typing import Any, Iterator as PyIterator

class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass
    
    @abstractmethod
    def next(self) -> Any:
        pass

class Collection(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass

class ArrayIterator(Iterator):
    def __init__(self, items: list):
        self.items = items
        self.position = 0
    
    def has_next(self) -> bool:
        return self.position < len(self.items)
    
    def next(self) -> Any:
        result = self.items[self.position]
        self.position += 1
        return result

class ArrayCollection(Collection):
    def __init__(self):
        self.items = []
    
    def add(self, item: Any) -> None:
        self.items.append(item)
    
    def create_iterator(self) -> Iterator:
        return ArrayIterator(self.items)

collection = ArrayCollection()
collection.add(10)
collection.add(20)
collection.add(30)

it = collection.create_iterator()
while it.has_next():
    print(it.next(), end=" ")
print()
