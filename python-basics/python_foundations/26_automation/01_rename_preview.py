from pathlib import Path
for p in Path(".").glob("*.txt"):
    print("Would rename:", p, "->", p.with_name("processed_" + p.name))
