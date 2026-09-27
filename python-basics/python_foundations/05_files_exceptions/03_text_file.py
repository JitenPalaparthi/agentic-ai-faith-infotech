from pathlib import Path
p = Path("sample.txt")
p.write_text("hello\npython\n", encoding="utf-8")
print(p.read_text(encoding="utf-8"))
p.unlink()
