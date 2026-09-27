class Managed:
    def __enter__(self):
        print("enter")
        return self
    def __exit__(self, exc_type, exc, tb):
        print("exit")
        return False

with Managed():
    print("inside")
