from tkinter import *

root=Tk()

root.geometry("455x355")
f1= Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT, fill=Y)
f2=Frame(root,bg="grey",borderwidth=10,relief=SUNKEN)
f2.pack(side=TOP,fill=X)
f3=Frame(root,bg="white",borderwidth=8,relief=RAISED)
f3.pack(fill=BOTH)

l1=Label(f1,text="Project Tkinter - PyCharm")
l1.pack(pady=150)

l2=Label(f2,text="Welcome",font="Helvetica 16 bold",foreground="grey")
l2.pack()

l3=Label(f3,text="Write your code")
l3.pack(pady=150,padx=150)

root.mainloop()