def area(radius: float) -> float:
    """Return circle area."""
    return 3.14159 * radius ** 2

print(area(2.0))
print(area.__annotations__)
