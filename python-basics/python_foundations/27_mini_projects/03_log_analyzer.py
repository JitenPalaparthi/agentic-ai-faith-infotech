from collections import Counter

lines = [
    "INFO user-login",
    "ERROR db-timeout",
    "INFO user-login",
    "WARNING cache-miss",
]
levels = Counter(line.split()[0] for line in lines)
print(levels)
