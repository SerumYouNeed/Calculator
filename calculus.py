from random import randrange

def add():
    a = randrange(1, 101)
    b = randrange(1, 101)
    equals = a + b
    return (a, b, equals)

def substract():
    a = randrange(1, 101)
    b = randrange(1, 101)
    equals = a - b
    return (a, b, equals)

def multiply():
    a = randrange(0, 101)
    b = randrange(0, 101)
    equals = a * b
    return (a, b, equals)

def divide():
    a = randrange(1, 101)
    b = randrange(1, 101)
    equals = a / b
    return (a, b, equals)