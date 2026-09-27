class Subject:
    def __init__(self):
        self.listeners = []
    def subscribe(self, fn):
        self.listeners.append(fn)
    def emit(self, value):
        for fn in self.listeners:
            fn(value)

s = Subject()
s.subscribe(lambda v: print("got", v))
s.emit(42)
