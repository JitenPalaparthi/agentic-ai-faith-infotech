from langchain_core.tools import tool

@tool
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

@tool
def service_health(service: str) -> str:
    """Return demo health information for a service."""
    data = {"users": "UP", "orders": "DEGRADED"}
    return data.get(service.lower(), "UNKNOWN")

print(add.invoke({"a": 20, "b": 22}))
print(service_health.invoke({"service": "orders"}))
