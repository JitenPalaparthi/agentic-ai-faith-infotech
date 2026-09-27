from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

print(Point(1, 2))
