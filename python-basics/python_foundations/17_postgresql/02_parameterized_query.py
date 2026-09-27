import os, psycopg
dsn = os.getenv("DATABASE_URL")
if not dsn:
    raise SystemExit("Set DATABASE_URL first")
with psycopg.connect(dsn) as con:
    with con.cursor() as cur:
        cur.execute("SELECT %s::int + %s::int", (10, 20))
        print(cur.fetchone()[0])
