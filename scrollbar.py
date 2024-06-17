from tkinter import *

root=Tk()
root.geometry("455x355")
root.title("Scrollbar")
#For connecting a scrollbar to a widget:
# 1. widget(yscrollcommand = scrollbar.set)
# 2. scrollbar.config(command=widget.yview)

scrollbar=Scrollbar(root)
scrollbar.pack(fill=Y,side=RIGHT)

lbx=Listbox(root,yscrollcommand=scrollbar.set)
for i in range(344):
    lbx.insert(END,f"Item{i}")

lbx.pack()
scrollbar.config(command=lbx.yview)

root.mainloop()