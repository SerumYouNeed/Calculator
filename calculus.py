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
    equals = a - b
    equation = f"{a} - {b}"
    return (equals, equation)

def multiply():
    a = randrange(0, 11)
    b = randrange(0, 21)
    equals = a * b
    equation = f"{a} * {b}"
    return (equals, equation)

def divide():
    a = randrange(1, 51)
    b = randrange(2, 51)
    while (a % b != 0):
        a = randrange(1, 101)
        b = randrange(2, 51)
    equals = a / b
    equation = f"{a} / {b}"
    return (equals, equation)

def quiz():
    mode = randrange(1, 5)
    match mode:
        case 1:
            eq = add()
        case 2:
            eq = substract()
        case 3:
            eq = multiply()
        case 4:
            eq = divide()
    return eq

def challenge():
    equals1, equation1 = quiz()
    equals2, equation2 = quiz()
    equals3, equation3 = quiz()
    sign1 = sign_choice()
    sign2 = sign_choice()
    match sign1:
        case "+":
            mid1 = equals1 + equals2
        case "-":
            mid1 = equals1 - equals2
            while (mid1 < 0):
                equals1, equation1 = quiz()
                equals2, equation2 = quiz()
                mid1 = equals1 - equals2
        case "*":
            mid1 = equals1 * equals2
        case "/":
            mid1 = equals1 / equals2
            while (equals1 % equals2 != 0):
                equals1, equation1 = quiz()
                equals2, equation2 = quiz()
                mid1 = equals1 / equals2
    expresion = f"({equation1}) {sign1} ({equation2})"
    return (expresion, mid1) 
        
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