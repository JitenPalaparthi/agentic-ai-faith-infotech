import json
from pathlib import Path

DB = Path("todos.json")

def load():
    return json.loads(DB.read_text()) if DB.exists() else []

def save(items):
    DB.write_text(json.dumps(items, indent=2))

def main():
    items = load()
    while True:
        cmd = input("(a)dd (l)ist (q)uit: ").strip().lower()
        if cmd == "a":
            items.append({"task": input("Task: "), "done": False})
            save(items)
        elif cmd == "l":
            for i, item in enumerate(items, 1):
                print(i, "[x]" if item["done"] else "[ ]", item["task"])
        elif cmd == "q":
            break

if __name__ == "__main__":
    main()
