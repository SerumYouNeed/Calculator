from random import randrange
from account import player as user

def add():
    a = randrange(1, 101)
    b = randrange(1, 101)
    equals = a + b
    player = int(input(f"{a} + {b} = "))
    return checking(equals, player, user)

def substract():
    a = randrange(1, 101)
    b = randrange(1, 101)
    equals = a - b
    player = int(input(f"{a} - {b} = "))
    return checking(equals, player, user)

def multiply():
    a = randrange(0, 101)
    b = randrange(0, 101)
    equals = a * b
    player = int(input(f"{a} * {b} = "))
    return checking(equals, player, user)

def divide():
    a = randrange(1, 101)
    b = randrange(1, 101)
    equals = a / b
    player = int(input(f"{a} / {b} = "))
    return checking(equals, player, user)
    
def checking(equals, player, user):
    if equals == player:
        print("Corretct. I earned 1 point.")
        user.update_score(1)
        return True
    else:
        print(f"Incorrect. You earned {user.score} points.")
        return False