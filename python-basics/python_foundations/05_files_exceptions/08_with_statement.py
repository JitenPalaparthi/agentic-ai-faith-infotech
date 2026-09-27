with open("temp.txt", "w", encoding="utf-8") as f:
    f.write("managed resource")
with open("temp.txt", encoding="utf-8") as f:
    print(f.read())

import os
os.remove("temp.txt")
