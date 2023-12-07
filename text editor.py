import sys
import tkinter.filedialog
from tkinter import *
from tkinter import filedialog as fd, font

rootwin = Tk("Text Editor")
rootwin.title("Text Editor")
text = Text(rootwin)
text.grid()


def save_to_file():
    global text
    txt = text.get("1.0", "end-1c")
    savelocation = tkinter.filedialog.asksaveasfile()
    if savelocation:
        print(savelocation.name)
        with open(savelocation.name, "w+") as file1:
            file1.write(txt)

def font_helvetica():
    global text
    text.config(font="Helvetica")

def font_courier():
    global text
    text.config(font="Courier")

button_save = Button(rootwin, text="save", command=save_to_file)
button_save.grid()

font_menu = Menu(rootwin, tearoff=0)
font_menu.add_checkbutton(label="Courier", variable=Courier, command=font_courier)
font_menu.add_checkbutton(label="Helvetica", variable=Helvetica, command=font_helvetica)

menu_bar = Menu(rootwin)
menu_bar.add_cascade(label="font", menu=font_menu)
rootwin.config(menu=menu_bar)

rootwin.mainloop()
