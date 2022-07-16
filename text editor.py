import sys
import tkinter.filedialog
from tkinter import *
from tkinter import filedialog as fd, font

rootwin = Tk("Text Editor")
rootwin.title("Text Editor")
text = Text(rootwin)
text.grid()


def savedb():
    global text
    txt = text.get("1.0", "end-1c")
    savelocation = tkinter.filedialog.asksaveasfile()
    print(savelocation.name)
    file1 = open(savelocation.name, "w+")
    file1.write(txt)
    file1.close()
button=Button(rootwin,text="save", command=savedb)
button.grid()

def fontHelvetica():
    global text
    text.config(font="Helvetica")

def fontCourier():
    global text
    text.config(font="Courier")
font=Menubutton(rootwin,text="font")
font.grid()
font.menu=Menu(font,tearoff=0)
font["menu"]=font.menu
Helvetica=IntVar()
Arial=IntVar()
Times=IntVar()
Courier=IntVar()

font.menu.add_checkbutton(label="Courier",variable=Courier,command=fontCourier)
font.menu.add_checkbutton(label="Helvetica",variable=Helvetica,command=fontHelvetica)
rootwin.mainloop()
