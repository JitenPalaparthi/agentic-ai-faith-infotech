class Animal:
    def speak(self):
        return "?"

class Dog(Animal):
    def speak(self):
        return "woof"

print(Dog().speak())
