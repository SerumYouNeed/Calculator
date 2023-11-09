import tkinter as tk


root = tk.Tk()
root.geometry("700x450")
root.title("World of algebra!")
root.configure(bg="pale turquoise")

b1 = tk.Button(
    root,
    background="cyan", 
    activebackground="cyan4",
    foreground="black",
    activeforeground="black",
    highlightthickness=5,
    highlightcolor="YELLOW",
    highlightbackground="green",
    width=18,
    height=2,
    border=3,
    borderwidth=3,
    cursor="hand2",
    font=("Helvatica", 14, "bold")
)

b2 = tk.Button(
    root,
    background="cyan", 
    activebackground="cyan4",
    foreground="black",
    activeforeground="black",
    highlightthickness=5,
    highlightcolor="YELLOW",
    highlightbackground="green",
    width=18,
    height=2,
    border=3,
    borderwidth=3,
    cursor="hand2",
    font=("Helvatica", 14, "bold")
)

l1 = tk.Label(
    root, 
    text="Welcome in \"The world of algebra\"", 
    bg="pale turquoise", 
    foreground="black", 
    font=("size, 22"), 
    pady=20
)

l2 = tk.Label(
    root, 
    text="If you have an account, please:", 
    bg="pale turquoise", 
    foreground="black", 
    font=("Helvatica", "22"), 
    pady=20
)

l3 = tk.Label(
    root, 
    text="If not, please:", 
    bg="pale turquoise", 
    foreground="black", 
    font=("size, 22"), 
    pady=20
)