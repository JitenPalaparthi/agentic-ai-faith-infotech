from pathlib import Path
here = Path(".")
for item in list(here.iterdir())[:5]:
    print(item)
