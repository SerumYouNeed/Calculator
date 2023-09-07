import csv
from account import account

def log_in():
    try:
        with open("players.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=["login","password","score"])
            login = input("Please, enter login: ")
            for row in reader:
                if row["login"] == login:
                    password = input("Please, enter password: ")
                    if row["password"] == password:
                        current_player = account(login)
                        print(f"Welcome {current_player.name}")
                        return current_player
                    else:
                        print("Incorect password")
                else:
                    print("Incorrect user")
    except FileNotFoundError:
        pass

# Przeprowadź walidację podwójnych loginów i haseł
def sign_up():
    try:
        with open("players.csv", "a") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["login","password","score"])
            login = input("Please, enter your nick: ")
            password = input("Please, enter unique password: ")
            score = 0
            writer.writerow({"login": login, "password": password, "score": score})
    except FileNotFoundError:
        pass
