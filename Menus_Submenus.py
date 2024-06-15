from tkinter import *

def myfunc():
    print(" I am a function ")

root = Tk()
root.geometry('744x566')
root.title("Menus and Submenus")

#use these to create a non-dropdown menu

#my_menu= Menu(root)
#my_menu.add_command(label="file",command=myfunc)
#my_menu.add_command(label="exit",command=quit)
#root.config(menu=my_menu)

mainmenu = Menu(root)

m1= Menu(mainmenu,tearoff=0)#tearoff removes "--------" from dropdown
m1.add_command(label="New",command=myfunc)
m1.add_command(label="Save",command=myfunc)
m1.add_separator()#adds a separator line
m1.add_command(label="View",command=myfunc)
m1.add_command(label="Print",command=myfunc)

mainmenu.add_cascade(label="File",menu=m1)

m2= Menu(mainmenu,tearoff=0)#tearoff removes "--------" from dropdown
m2.add_command(label="Cut",command=myfunc)
m2.add_command(label="Copy",command=myfunc)
m2.add_command(label="Paste",command=myfunc)
m2.add_separator()#adds a separator line
m2.add_command(label="Undo",command=myfunc)

root.config(menu=mainmenu)

mainmenu.add_cascade(label="Edit",menu=m2)


root.mainloop()