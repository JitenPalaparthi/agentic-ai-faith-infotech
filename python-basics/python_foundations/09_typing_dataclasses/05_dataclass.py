from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    active: bool = True

print(User(1, "Ada"))
