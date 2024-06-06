from tkinter import *

root=Tk()
root.geometry("655x333")

def hello():
    print("Hello")

f1=Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
f1.pack(side=LEFT,anchor="nw")

b1=Button(f1,fg="red",text="Print Now",command=hello)
b1.pack(padx=23)

root.mainloop()