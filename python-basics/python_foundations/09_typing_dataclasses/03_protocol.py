from typing import Protocol

class HasName(Protocol):
    name: str

def show(obj: HasName):
    print(obj.name)

class User:
    name = "Ada"

show(User())
