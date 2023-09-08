from random import randrange
from account import user

def add():
    a = randrange(1, 101)
    b = randrange(1, 101)
    equals = a + b
    guess = int(input(f"{a} + {b} = "))
    return checking(equals, guess)

def substract():
    a = randrange(1, 101)
    b = randrange(1, 101)
    equals = a - b
    guess = int(input(f"{a} - {b} = "))
    return checking(equals, guess)

def multiply():
    a = randrange(0, 101)
    b = randrange(0, 101)
    equals = a * b
    guess = int(input(f"{a} * {b} = "))
    return checking(equals, guess)

def divide():
    a = randrange(1, 101)
    b = randrange(1, 101)
    equals = a / b
    guess = int(input(f"{a} / {b} = "))
    return checking(equals, guess)
    
def checking(equals, guess):
    if equals == guess:
        print("Corretct. I earned 1 point.")
        return True
    else:
        print(f"Incorrect. You earned {user.score} points.")
        return False