from random import randrange
import math

def add():
    a = randrange(1, 101)
    b = randrange(1, 101)
    equals = a + b
    sign = " + "
    return (a, b, equals, sign)

def substract():
    a = randrange(1, 101)
    b = randrange(1, 101)
    equals = a - b
    sign = " - "
    return (a, b, equals, sign)

def multiply():
    a = randrange(0, 101)
    b = randrange(0, 101)
    equals = a * b
    sign = " * "
    return (a, b, equals, sign)

def divide():
    a = randrange(1, 101)
    b = randrange(1, 101)
    equals = a / b
    sign = " / "
    return (a, b, equals, sign)

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

def convert():
    numbers = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9,
               "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}
    
    roman = list(numbers.keys())
    arabic = list(numbers.values())

    how_large = randrange(1, 10001)
    if how_large in arabic:
        pass
    else:
        if how_large >= 1000:
            thous = math.floor(how_large / 1000)
            hund = math.floor((how_large - thous) / 100)
            tens = math.floor((how_large - ))
    to_convert = randrange(len(roman))
    