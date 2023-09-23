import tkinter as tk
from logs import *

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.pack()

        self.my_label = tk.Label(text="Welcome in \"The world of algebra\"", foreground="black", font=("size, 22"), pady=20)
        self.my_label.pack()
        
        self.my_label = tk.Label(text="If you have an account, please:", foreground="black", font=("size, 18"), pady=15)
        self.my_label.pack()

        self.log_button = tk.Button(text="Logging", background="orange", height=2, width=18, font=("size, 14"), command=self.clear_frame)
        self.log_button.pack()

        self.my_label3 = tk.Label(text="----- OR -----", foreground="black", font=("size, 18"), pady=10)
        self.my_label3.pack()

        self.sign_button = tk.Button(text="Sign up", background="orange", height=2, width=18, font=("size, 14"))
        self.sign_button.pack()

        self.entrythingy = tk.Entry()
        #self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())
        
    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def logging(self):
        self.clear_frame()
        
'''
def log_in_button(label):
    label.config(text="Please, enter your username: ")
    log_button.destroy()
    my_label2.destroy()
    sign_button.destroy()

    username_e = Entry(root)
    username_e.pack()
    username_e.insert(0, "Username:" )

root = Tk()
root.geometry("700x450")
root.title("World of algebra!")

my_label = Label(root, text=labels.welcome, foreground="blue", font=("size, 18", "bold, true"))
my_label.grid(row=0, column=0)

#password_e = Entry(root)
#password_e.pack()

log_button = Button(root, text="Logging", command=lambda: log_in_button(my_label))
log_button.grid(row=1, column=0)

my_label2 = Label(root, text="----- OR -----", foreground="blue", font=("size, 18", ))
my_label2.grid(row=2, column=0)

sign_button = Button(root, text="Sign up")
sign_button.grid(row=3, column=0)

root.mainloop()
'''