import sqlite3
con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
con.execute("INSERT INTO users(name) VALUES (?)", ("Ada",))
print(con.execute("SELECT * FROM users").fetchall())
con.close()
