from random import randrange

def add():
    a = randrange(1, 101)
    b = randrange(1, 101)
    equals = a + b
    equation = f"{a} + {b}"
    return (equals, equation)

def substract():
    a = randrange(1, 101)
    b = randrange(1, 101)
    while (a - b < 0):
        a = randrange(1, 101)
        b = randrange(2, 101)
    equals = a / b
    equation = f"{a} - {b}"
    return (equals, equation)

def multiply():
    a = randrange(0, 101)
    b = randrange(0, 11)
    equals = a * b
    equation = f"{a} * {b}"
    return (equals, equation)

def divide():
    a = randrange(1, 101)
    b = randrange(2, 51)
    while (a % b != 0):
        a = randrange(1, 101)
        b = randrange(2, 51)
    equals = a / b
    equation = f"{a} / {b}"
    return (equals, equation)

def quiz():
    mode = randrange(1, 5)
    if mode == 1:
        add()
    elif mode == 2:
        substract()
    elif mode == 3:
        multiply()
    elif mode == 4:
        divide()
    else:
        print("Quiz cannot run.")

def challenge():
    equals1, equation1 = mode()
    equals2, equation2 = mode()
    equals3, equation3 = mode()
    sign1 = sign_choice()
    sign2 = sign_choice()
    if sign1 == "+":
        mid1 = equals1 + equals2
    elif sign1 == "-":
        mid1 = equals1 - equals2
    elif sign1 == "*":
        mid1 = equals1 * equals2
    elif sign1 == "/":
        mid1 = equals1 / equals2
    if sign2 == "+":
        equals = mid1 + equals3
    elif sign2 == "-":
        equals = mid1 - equals3
    elif sign2 == "*":
        equals = mid1 * equals3
    elif sign2 == "/":
        equals = mid1 / equals3
    expresion = f"({equation1}) {sign1} ({equation2}) {sign2} ({equation3})"
    return (expresion, equals) 

def mode():
    mode = randrange(1, 5)
    if mode == 1:
        return add()
    elif mode == 2:
        return substract()
    elif mode == 3:
        return multiply()
    elif mode == 4:
        return divide()
        
def sign_choice():
    mode = randrange(1, 5)
    if mode == 1:
        sign = "+"
    elif mode == 2:
        sign = "-"
    elif mode == 3:
        sign = "*"
    elif mode == 4:
        sign = "/"
    return sign