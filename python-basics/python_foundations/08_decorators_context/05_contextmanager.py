from contextlib import contextmanager

@contextmanager
def resource():
    print("acquire")
    try:
        yield "resource"
    finally:
        print("release")

with resource() as r:
    print(r)
