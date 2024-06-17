from tkinter import *


def add():
    global i #i can be modified now
    lbx.insert(ACTIVE,f"{i}")#inserts above current ACTIVE list item
    i+=1
i=0  

root=Tk()
root.geometry("455x355")
root.title("ListBox")


lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"First Item")

Button(root,text="Add Item",command=add).pack()


root.mainloop()