class Math:
    count = 0

    @classmethod
    def create(cls):
        cls.count += 1
        return cls()

    @staticmethod
    def square(x):
        return x*x

Math.create()
print(Math.count, Math.square(5))
