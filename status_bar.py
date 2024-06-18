#There is no specific widget available for StatusBar in Tkinter
#It is a widget created using Label and Buttons only.

from tkinter import *

def upload():
    statusvar.set("Busy")
    sbar.update()#this is a needed line to show Busy On StatusBar
    import time
    time.sleep(2)
    statusvar.set("Ready Now")

root=Tk()
root.geometry("455x355")
root.title("StatusBar")


statusvar=StringVar()
statusvar.set("Ready")
sbar=Label(root,textvariable=statusvar,relief=SUNKEN,anchor=W)
sbar.pack(side=BOTTOM,fill=X)
Button(root,text="Update",command=upload).pack()

root.mainloop()