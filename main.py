import calculus as calc
import tkinter as tk
from account import user
from screens import root, MyButton, MyLabel, MyEntry, MyRadio, helv36, helv28
import db

database = r"users_db.db"
# create a database connection
conn = db.create_connection(database)
# create tables
if conn is not None:
# create projects table
    db.create_table(conn, db.sql_create_users_table)
else:
    print("Error! cannot create the database connection.")

def solution_checker(equals, var, mode):
    clear_frame(root)
    if equals == var:
        user.update_points(1)
        root.configure(bg="chartreuse2")
        MyLabel("Corretct. You earned 1 point.", color="chartreuse2").pack()
        MyButton("Next", color="chartreuse4", activebackground="dark green", command=lambda: select_mode(mode)).pack()      
    else:
        root.configure(bg="red")
        MyLabel("Incorrect. Your score is: " + str(user.points), color="red").pack()
        if user.mode == "exercise":
            MyButton("END", color="red3", activebackground="red4", command=lambda: radiobutton_screen()).pack()      
        else:
            # Because fetchone() is returning a tuple-like object
            best_user_score = db.get_score(conn, (user.name,))[0]
            if best_user_score < user.points:
                db.update_score(conn, (user.points, user.name,))
            MyButton("END", color="red3", activebackground="red4", command=lambda: score_table()).pack()      
        return False
    
def score_table():
    clear_frame(root)
    root.configure(bg="DarkOrchid1")
    MyLabel("BEST SCORES", color="DarkOrchid1", font=helv36).pack()
    for player in db.print_scores(conn):
        MyLabel(text=player, color="DarkOrchid1", font=helv28, x=30).pack()
    MyButton("Back", color="DarkOrchid3", activebackground="DarkOrchid4", command=log_click).pack()

def radiobutton_screen():
    clear_frame(root)
    root.configure(bg="SkyBlue1")
    var = tk.StringVar()
    MyLabel("Please, select game mode from the list below:").pack()
    MyRadio(text="+ Add", variable=var, value="1").pack()
    MyRadio(text="- Substract", variable=var, value="2").pack()
    MyRadio(text="* Multiple", variable=var, value="3").pack()
    MyRadio(text="/ Divide", variable=var, value="4").pack()
    MyRadio(text="Quiz", variable=var, value="5").pack()
    MyRadio(text="CHALLENGE", variable=var, value="6").pack()
    MyButton("PLAY", command=lambda: select_mode(getter(var))).pack()

def select_mode(mode):
    var = tk.IntVar()
    root.configure(bg="SkyBlue1")
    if mode == "1":
        user.mode = "exercise"
        equals, equation = calc.add()     
        clear_frame(root)
        MyLabel(text=equation).pack()
        MyEntry(textvariable=var).pack() 
        MyButton("CHECK", command=lambda: solution_checker(equals, getter(var), mode)).pack()
    elif mode == "2":
        user.mode = "exercise"
        equals, equation = calc.substract()     
        clear_frame(root)
        MyLabel(text=equation).pack()
        MyEntry(textvariable=var).pack() 
        MyButton("CHECK", command=lambda: solution_checker(equals, getter(var), mode)).pack()
    elif mode == "3":
        user.mode = "exercise"
        equals, equation = calc.multiply()     
        clear_frame(root)
        MyLabel(text=equation).pack()
        MyEntry(textvariable=var).pack() 
        MyButton("CHECK", command=lambda: solution_checker(equals, getter(var), mode)).pack()
    elif mode == "4":
        user.mode = "exercise"
        equals, equation = calc.divide()     
        clear_frame(root)
        MyLabel(text=equation).pack()
        MyEntry(textvariable=var).pack() 
        MyButton("CHECK", command=lambda: solution_checker(equals, getter(var), mode)).pack()
    elif mode == "5":
        user.mode = "exercise"
        equals, equation = calc.quiz()     
        clear_frame(root)
        MyLabel(text=equation).pack()
        MyEntry(textvariable=var).pack() 
        MyButton("CHECK", command=lambda: solution_checker(equals, getter(var), mode)).pack()
    elif mode == "6":
        user.mode = "challenge"
        expresion, equals = calc.challenge()     
        clear_frame(root)
        MyLabel(text=expresion).pack()
        MyEntry(textvariable=var).pack() 
        MyButton("CHECK", command=lambda: solution_checker(equals, getter(var), mode)).pack()

def sign_in(name, password):
    user.name = name
    user.password = password
    with conn:
        # create a new user
        player = (name, password, user.score)
        db.create_user(conn, player)
    clear_frame(root)
    MyLabel("Success! Now you can log in.").pack()
    MyButton("Logging", log_click).pack()
    
def log_in(name, password):
    user.name = name
    user.password = password
    counter = 3
    try:
        with conn:
            player = (name, password)
            if db.log_user(conn, player):
                clear_frame(root)
                MyLabel("Welcome " + name + " !!!", font=helv36).pack()
                radiobutton_screen()
            else:
                clear_frame(root)
                if counter > 0:
                    counter -= 1
                    MyLabel(text="Incorect. Please, try again.", foreground="red").pack()
                    MyButton("Logging", command=log_click).pack()   
                else:
                    MyLabel(text="Access denied!!!", foreground="red").pack()
    except FileNotFoundError:
        pass

def getter(par):
    return par.get()

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def log_click(): 
    clear_frame(root)
    root.configure(bg="SkyBlue1")
    username = tk.StringVar()
    MyEntry(textvariable=username).pack()
    password = tk.StringVar()
    tk.Entry(root, width=20, font=helv28, bd=10, show="*", textvariable=password).pack()   
    MyButton("Enter", lambda: log_in(getter(username), getter(password))).pack()

def sign_click(): 
    clear_frame(root)
    root.configure(bg="SkyBlue1")
    username = tk.StringVar()
    MyEntry(textvariable=username).pack()
    password = tk.StringVar()
    MyEntry(textvariable=password).pack()
    MyButton("Enter", lambda: sign_in(getter(username), getter(password))) .pack()  

MyLabel("Welcome in").pack() 
MyLabel("\"The world of algebra\"", font=helv36).pack()
MyLabel("If you have an account, please:").pack()
MyButton("Logging", log_click).pack()
MyLabel("If not, please:").pack()
MyButton("Sign up", sign_click).pack()

root.mainloop()