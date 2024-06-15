from tkinter import *

root = Tk()
root.title("Radiobuttons")
root.geometry("455x233")

var = IntVar()

Label(root,text="What would you like to eat",justify=LEFT,padx=14).pack()
radio=Radiobutton(root,text="Biryani",padx=14,variable=var,value=1).pack(anchor="w")
radio=Radiobutton(root,text="Noodles",padx=14,variable=var,value=2).pack(anchor="w")
radio=Radiobutton(root,text="Burger",padx=14,variable=var,value=3).pack(anchor="w")
radio=Radiobutton(root,text="Grilled Chicken",padx=14,variable=var,value=4).pack(anchor="w")

Button(text="Order Now").pack()
root.mainloop()