class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self, a, b):
        self.a = a
        self.b = b


    def f(self):
        return 'hello world'



x = MyClass(3,4)
print(x.i)
print(x.a)
print(x.b)
print(x.f())


class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)

