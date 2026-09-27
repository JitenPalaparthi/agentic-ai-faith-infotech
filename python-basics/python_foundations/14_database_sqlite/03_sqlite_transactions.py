import sqlite3
con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE accounts(id INTEGER, balance INTEGER)")
con.executemany("INSERT INTO accounts VALUES (?,?)", [(1,100),(2,50)])
try:
    with con:
        con.execute("UPDATE accounts SET balance=balance-20 WHERE id=1")
        con.execute("UPDATE accounts SET balance=balance+20 WHERE id=2")
except sqlite3.DatabaseError:
    print("rollback")
print(con.execute("SELECT * FROM accounts").fetchall())
