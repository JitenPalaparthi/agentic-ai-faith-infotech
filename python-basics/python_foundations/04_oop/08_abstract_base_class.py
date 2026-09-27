from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def save(self, item):
        ...

class MemoryRepository(Repository):
    def save(self, item):
        print("saved", item)

MemoryRepository().save({"id": 1})
