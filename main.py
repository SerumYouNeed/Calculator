import calculus as calc
import tkinter as tk
import tkinter.ttk as ttk
from account import user
from screens import root, b1, b2, l1, l2, l3
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
        tk.Label(root, text="Corretct. You earned 1 point.", foreground="black", font=("size, 22")).pack()
        tk.Button(root, text="Next", background="orange", height=2, width=18, font=("size, 14"), command=lambda: select_mode(mode)).pack()      
    else:
        # Because fetchone() is returning a tuple-like object
        best_user_score = db.get_score(conn, (user.name,))[0]
        if best_user_score < user.points:
            db.update_score(conn, (user.points, user.name,))
        tk.Label(root, text="Incorrect. Your score is: " + str(user.points), foreground="black", font=("size, 22")).pack()
        tk.Button(root, text="END", background="orange", height=2, width=18, font=("size, 14"), command=lambda: score_table()).pack()      
        return False
    
def score_table():
    clear_frame(root)
    for player in db.print_scores(conn):
        tk.Label(root, text=player, foreground="black", font=("size, 22")).pack()

def select_mode(mode):
    var = tk.IntVar()
    if mode == "1":
        a, b, equals = calc.add()     
        clear_frame(root)
        tk.Label(root, text=str(a) + " + " + str(b) + " =", foreground="black", font=("size, 26")).pack()
        tk.Entry(root, width=20, font=("size, 22"), bd=5, textvariable=var).pack() 
        tk.Button(root, text="CHECK", background="orange", height=2, width=18, font=("size, 14"), command=lambda: solution_checker(equals, getter(var), mode)).pack()
    elif mode == "2":
        a, b, equals = calc.substract()     
        clear_frame(root)
        tk.Label(root, text=str(a) + " - " + str(b) + " =", foreground="black", font=("size, 26")).pack()
        tk.Entry(root, width=20, font=("size, 22"), bd=5, textvariable=var).pack() 
        tk.Button(root, text="CHECK", background="orange", height=2, width=18, font=("size, 14"), command=lambda: solution_checker(equals, getter(var), mode)).pack()
    elif mode == "3":
        a, b, equals = calc.multiply()     
        clear_frame(root)
        tk.Label(root, text=str(a) + " * " + str(b) + " =", foreground="black", font=("size, 26")).pack()
        tk.Entry(root, width=20, font=("size, 22"), bd=5, textvariable=var).pack() 
        tk.Button(root, text="CHECK", background="orange", height=2, width=18, font=("size, 14"), command=lambda: solution_checker(equals, getter(var), mode)).pack()
    elif mode == "4":
        a, b, equals = calc.divide()     
        clear_frame(root)
        tk.Label(root, text=str(a) + " / " + str(b) + " =", foreground="black", font=("size, 26")).pack()
        tk.Entry(root, width=20, font=("size, 22"), bd=5, textvariable=var).pack() 
        tk.Button(root, text="CHECK", background="orange", height=2, width=18, font=("size, 14"), command=lambda: solution_checker(equals, getter(var), mode)).pack()
    elif mode == "5":
        a, b, equals, sign = calc.quiz()     
        clear_frame(root)
        tk.Label(root, text=str(a) + sign + str(b) + " =", foreground="black", font=("size, 26")).pack()
        tk.Entry(root, width=20, font=("size, 22"), bd=5, textvariable=var).pack() 
        tk.Button(root, text="CHECK", background="orange", height=2, width=18, font=("size, 14"), command=lambda: solution_checker(equals, getter(var), mode)).pack()
    elif mode == "6":
        a, b, equals = calc.challenge()     
        clear_frame(root)
        tk.Label(root, text=str(a) + " + " + str(b) + " =", foreground="black", font=("size, 26")).pack()
        tk.Entry(root, width=20, font=("size, 22"), bd=5, textvariable=var).pack() 
        tk.Button(root, text="CHECK", background="orange", height=2, width=18, font=("size, 14"), command=lambda: solution_checker(equals, getter(var), mode)).pack()

def sign_in(name, password):
    user.name = name
    user.password = password
    with conn:
        # create a new user
        player = (name, password, user.score)
        db.create_user(conn, player)
    clear_frame(root)
    tk.Label(root, text="Success! Now you can log in.", foreground="green", font=("size, 22"), pady=20).pack()
    tk.Button(root, text="Logging", background="orange", height=2, width=18, font=("size, 14"), command=log_click).pack()   
    
def log_in(name, password):
    user.name = name
    user.password = password
    counter = 3
    try:
        with conn:
            player = (name, password)
            if db.log_user(conn, player):
                clear_frame(root)
                var = tk.StringVar()
                tk.Label(root, text="Welcome " + name + " !!!", foreground="green", font=("size, 22"), pady=20).pack()
                tk.Label(root, text="Please, select game mode from the list below:", foreground="black", font=("size, 22")).pack()
                tk.Radiobutton(root, text="+ Add", variable=var, value="1", font=("size, 16")).pack()
                tk.Radiobutton(root, text="- Substract", variable=var, value="2", font=("size, 16")).pack()
                tk.Radiobutton(root, text="* Multiple", variable=var, value="3", font=("size, 16")).pack()
                tk.Radiobutton(root, text="/ Divide", variable=var, value="4", font=("size, 16")).pack()
                tk.Radiobutton(root, text="Quiz", variable=var, value="5", font=("size, 16")).pack()
                tk.Radiobutton(root, text="CONVERT", variable=var, value="5", font=("size, 16")).pack()
                tk.Button(root, text="PLAY", background="orange", height=2, width=18, font=("size, 14"), command=lambda: select_mode(getter(var))).pack()
            else:
                clear_frame(root)
                if counter > 0:
                    counter -= 1
                    tk.Label(root, text="Incorect. Please, try again.", foreground="green", font=("size, 22"), pady=20).pack()
                    tk.Button(root, text="Logging", background="orange", height=2, width=18, font=("size, 14"), command=log_click).pack()
                else:
                    tk.Label(root, text="Access denied!!!", foreground="green", font=("size, 22"), pady=20).pack()
    except FileNotFoundError:
        pass

def getter(par):
    return par.get()

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def log_click(): 
    clear_frame(root)
    username = tk.StringVar()
    tk.Entry(root, width=20, font=("size, 22"), bd=5, show="*", textvariable=username).pack()
    password = tk.StringVar()
    tk.Entry(root, width=20, font=("size, 22"), bd=5, show="*", textvariable=password).pack()   
    tk.Button(root, text="Enter", background="orange", height=2, width=18, font=("size, 14"), command=lambda: log_in(getter(username), getter(password))).pack()

def sign_click(): 
    clear_frame(root)
    username = tk.StringVar()
    tk.Entry(root, width=20, font=("size, 22"), bd=5, textvariable=username).pack()
    password = tk.StringVar()
    tk.Entry(root, width=20, font=("size, 22"), bd=5, textvariable=password).pack()   
    tk.Button(root, text="Enter", background="orange", height=2, width=18, font=("size, 14"), command=lambda: sign_in(getter(username), getter(password))).pack()

l1.pack()
l2.pack()
b1.config(text="Logging", command=log_click)
b1.pack()
l3.pack()
b2.config(text="Sign up", command=sign_click)
b2.pack()

root.mainloop()