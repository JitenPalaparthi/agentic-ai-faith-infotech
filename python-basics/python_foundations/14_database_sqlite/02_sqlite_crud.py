import sqlite3
con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE items(id INTEGER PRIMARY KEY, name TEXT)")
con.executemany("INSERT INTO items(name) VALUES (?)", [("A",), ("B",)])
con.execute("UPDATE items SET name=? WHERE id=?", ("AA", 1))
print(con.execute("SELECT * FROM items").fetchall())
con.execute("DELETE FROM items WHERE id=?", (2,))
print(con.execute("SELECT * FROM items").fetchall())
