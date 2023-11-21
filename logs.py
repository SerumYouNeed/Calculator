challenge
walidacja hasel i loginow

equals1, equation1 = mode()
    equals2, equation2 = mode()
    equals3, equation3 = mode()
    sign1 = sign_choice()
    sign2 = sign_choice()
    if sign1 == "+":
        mid1 = equals1 + equals2
    elif sign1 == "-":
        mid1 = equals1 - equals2
        while mid1 < 0:
            equals1, equation1 = mode()
            equals2, equation2 = mode()
            mid1 = equals1 - equals2
    elif sign1 == "*":
        mid1 = equals1 * equals2
    elif sign1 == "/":
        mid1 = equals1 / equals2
        while equals1 % equals2 == 0:
            equals1, equation1 = mode()
            equals2, equation2 = mode()
            mid1 = equals1 / equals2
    if sign2 == "+":
        equals = mid1 + equals3
    elif sign2 == "-":
        equals = mid1 - equals3
        while equals < 0:
            equals3, equation3 = mode()
            equals = mid1 - equals3
    elif sign2 == "*":
        equals = mid1 * equals3
    elif sign2 == "/":
        equals = mid1 / equals3
        while mid1 % equals3 == 0:
            equals3, equation3 = mode()
            equals = mid1 / equals3
    expresion = f"({equation1}) {sign1} ({equation2}) {sign2} ({equation3})"
    return (expresion, equals)