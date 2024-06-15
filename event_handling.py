from tkinter import *

def click(event):
    print("You clicked on the button")

root = Tk()
root.title("Events in Tkinter")
root.geometry("455x355")

widget = Button(root,text="click me")
widget.pack()

widget.bind('<Button-1>',click)#binding an event to button "click me"
widget.bind("<Double-1>",quit)#quits GUI on double click

root.mainloop()