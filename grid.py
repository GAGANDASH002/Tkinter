from tkinter import *

root=Tk()
root.geometry("455x355")

def getvals():
    print("username:",userval.get())
    print("password:",passval.get())

l1= Label(root,text="Username")
l2= Label(root,text="Password")
l1.grid()
l2.grid(row=1)

#variable classes in tkinter
#BooleanVar,DoubleVar,IntVar,StringVar

#ENTRYWIDGET:

userval=StringVar()
passval=StringVar()

userentry=Entry(root,textvariable=userval)
passentry=Entry(root,textvariable=passval)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

b1=Button(root,text="Submit",command=getvals).grid()
root.mainloop()