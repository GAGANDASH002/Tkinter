from tkinter import *
import tkinter.messagebox as tmsg

def myfunc():
    print(" I am a function ")

def help():
    print("I will help you")
    a=tmsg.showinfo("Help","We Will help you with this GUI")
    #print(a) #return value of showinfo() is "ok"

def rate():
    val= tmsg.askquestion("Was your experience good","You used this GUI..Was your experience good")
    #print(val) #returns "yes" or "no"
    if val=="yes":
        msg="Great.Rate us on appstore please"
    else:
        msg="Let us know what went wrong"
    tmsg.showinfo("Experience",msg)

def explore():
    ans= tmsg.askretrycancel("Explore our apps","There was an unprecedented error.")
    if ans:
        print("Error! we will let you know soon")
    else:
        print("Have a good day!")
        
root = Tk()
root.geometry('744x566')
root.title("Menus and Submenus")


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

mainmenu.add_cascade(label="Edit",menu=m2)

m3= Menu(mainmenu,tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="Rate us",command=rate)
m3.add_command(label="Explore other apps?",command=explore)
mainmenu.add_cascade(label="Help",menu=m3)

root.config(menu=mainmenu)


root.mainloop()