from enum import Enum, auto
class Status(Enum):
    NEW = auto()
    DONE = auto()
print(Status.NEW)
