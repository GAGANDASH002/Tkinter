from tkinter import *

root = Tk()

#Width x Height
root.geometry("444x234")

#width,height
root.minsize(200,100)
root.maxsize(800,700)

l1= Label(text="This is a sample GUI")
l1.pack()

root.mainloop()