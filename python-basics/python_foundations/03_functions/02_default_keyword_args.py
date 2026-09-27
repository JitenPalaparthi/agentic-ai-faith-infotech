def connect(host="localhost", port=5432, *, timeout=5):
    print(host, port, timeout)

connect()
connect("db.internal", timeout=10)
