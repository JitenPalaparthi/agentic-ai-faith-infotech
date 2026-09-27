def normalize(value: str | int | None) -> str:
    return "" if value is None else str(value).strip()
print(normalize(10))
