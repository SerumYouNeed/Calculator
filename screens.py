import tkinter as tk
from tkinter import font

root = tk.Tk()
root.geometry("700x550")
root.title("World of algebra!")
root.configure(bg="SkyBlue1")

helv36 = font.Font(family='Helvetica', size=36, weight='bold')
helv28 = font.Font(family='Helvetica', size=28, weight='bold')
helv18 = font.Font(family='Helvetica', size=18, weight='bold')

class MyRadio(tk.Radiobutton):
    def __init__(self, text, variable, value, bg="SkyBlue1", activebackground="RoyalBlue4", font=helv18):
        self.text = text
        self.variable = variable
        self.value = value
        self.bg = bg
        self.activebackground = activebackground
        self.font = font
        super().__init__()
        self['text'] = self.text
        self['variable'] = self.variable
        self['value'] = self.value
        self['bg'] = self.bg
        self['activebackground'] = self.activebackground
        self['font'] = self.font

class MyEntry(tk.Entry):
    def __init__(self, textvariable, width=20, font=helv28, bd=10):
        self.width = width
        self.font = font
        self.bd = bd
        self.textvariable = textvariable
        super().__init__()
        self['width'] = self.width
        self['font'] = self.font
        self['bd'] = self.bd
        self['textvariable'] = self.textvariable

class MyButton(tk.Button):
    def __init__(self, text, command, font=("size, 20"), color="RoyalBlue1", activebackground="RoyalBlue4", foreground="black", activeforeground="black", cursor="hand2", width=16, height=1, x=0, y=7,**kwargs):
        self.text = text
        #self.row = row
        #self.column = col
        self.command = command
        self.font = font
        self.color = color
        self.activebackground = activebackground
        self.activeforeground = activeforeground
        self.foreground = foreground
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.cursor = cursor
        super().__init__()
        self['bg'] = self.color
        self['text'] = self.text
        self['command'] = self.command
        self['font'] = self.font
        self['activebackground'] = self.activebackground
        self['foreground'] = self.foreground
        self['activeforeground'] = self.activeforeground
        self['width'] = self.width
        self['height'] = self.height
        self['padx'] = self.x
        self['pady'] = self.y
        self['cursor'] = self.cursor
        #self.grid(row=self.row, column=self.column)
        
class MyLabel(tk.Label):
    def __init__(self, text, font=("size, 22"), color="SkyBlue1", foreground="black", x=5, y=20, **kwargs):
        self.text = text
        self.font = font
        self.color = color
        self.x = x
        self.y = y
        self.foreground = foreground
        super().__init__()
        self['bg'] = self.color
        self['text'] = self.text
        self['font'] = self.font
        self['padx'] = self.x
        self['pady'] = self.y
        self['foreground'] = self.foreground