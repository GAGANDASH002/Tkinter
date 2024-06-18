#resizing GUI taking user input

from tkinter import *

def update():
    print("Updating GUI")
    root.geometry(f"{width.get()}x{height.get()}")

root = Tk()
root.geometry("455x355")

width=StringVar()
height=StringVar()
Entry(root,textvariable=width).pack()
Entry(root,textvariable=height).pack()
Button(root,text="Apply",command=update).pack()


root.mainloop()

