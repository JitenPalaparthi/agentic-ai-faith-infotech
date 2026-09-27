class Engine:
    def start(self):
        return "engine started"

class Car:
    def __init__(self):
        self.engine = Engine()

print(Car().engine.start())
