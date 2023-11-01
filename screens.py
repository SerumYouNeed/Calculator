import tkinter as tk
import csv
from account import account




class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.pack()
        # Create the application variable.
        self.username = tk.StringVar()
        self.password = tk.StringVar()

    def log_in(self, name, password):
        try:
            with open("players.csv", "r") as csvfile:
                reader = csv.DictReader(csvfile, fieldnames=["login","password","score"])
                for row in reader:
                    if row["login"] == name:
                        if row["password"] == password:
                            name = account(name)
                            self.welcome_frame(name)
                        else:
                            return f"Incorect password"
                    else:
                        return f"Incorrect user"
        except FileNotFoundError:
            pass

    def starting_frame(self):
        self.l1 = tk.Label(self, text="Welcome in \"The world of algebra\"", foreground="black", font=("size, 22"), pady=20)
        self.l1.pack()
        
        self.l2 = tk.Label(self, text="If you have an account, please:", foreground="black", font=("size, 18"), pady=20)
        self.l2.pack()

        self.b1 = tk.Button(self, text="Logging", background="orange", height=2, width=18, font=("size, 14"), command=self.log_frame)
        self.b1.pack()

        self.l3 = tk.Label(self, text="----- or -----", foreground="black", font=("size, 18"), pady=20)
        self.l3.pack()

        self.b2 = tk.Button(self, text="Sign up", background="orange", height=2, width=18, font=("size, 14"), command=self.clear_frame)
        self.b2.pack()

    def clear_frame(self):
        for widget in self.winfo_children():
             widget.destroy()
        
    def log_frame(self):
        self.clear_frame()
        self.e1 = tk.Entry(width=20, font=("size, 22"), bd=5, show="*", textvariable=self.username).pack()
        self.e2 = tk.Entry(width=20, font=("size, 22"), bd=5, show="*", textvariable=self.password).pack()
        name = self.username.get()
        pwd = self.password.get() 
        self.b3 = tk.Button(self, text="Enter", background="orange", height=2, width=18, font=("size, 14"), command=self.log_in(name, pwd)).pack()

    def welcome_frame(self, name):
        self.clear_frame()
        self.l1 = tk.Label(self, text="Welcome" + name, foreground="green", font=("size, 22"), pady=20)
        self.l1.pack()

