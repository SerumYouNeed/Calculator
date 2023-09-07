import calculus as calc
import logs
import sys
import time
from os import system, name

def main():

    clear_screen()
    print("Welcome in \"The world of algebra\"!\n")

    incorrect_input = True
    while incorrect_input:
        choice_account = input("If you are new - press 1\n"
                           "If you have an account - press 2\n"
                           "For exit - press Q "
                           ).lower()
        if choice_account == "1":
            logs.sign_up()
            incorrect_input = False
        elif choice_account == "2":
            logs.log_in()
            incorrect_input = False
        elif choice_account == "q":
            incorrect_input = False
            clear_screen()
            sys.exit("See you next time!")
        else:
            print("Incorrect input. Please, try again\n\n")
            time.sleep(1)
            clear_screen()

    mode = input("Choose game mode:"
            "1. Adding."
            "2. Substracting."
            "3. Multiplying."
            "4. Division."
            "5. Quiz."
            "################"
            "6. Converter.")

    if mode == "1":
        while True:
            calc.add()
    elif mode == "2":
        while True:
            calc.substract()
    elif mode == "3":
        while True:
            calc.substract()
    elif mode == "4":
        while True:
            calc.divide()
    elif mode == "5":
        while True:
            calc.quiz()
    elif mode == "6":
        calc.converter()
    else:
        print("Try again")

# This function clears console depending on
def clear_screen():

    # For windows
    if name == "nt":
        _ = system("cls")

    # For os. name "posix" - mac and linux
    else:
        _ = system("clear")

if __name__ == "__main__":
    main()