def greet(name: str, times: int = 1) -> list[str]:
    return [f"Hello {name}" for _ in range(times)]
print(greet("Ada", 2))
