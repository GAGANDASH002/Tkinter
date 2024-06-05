from tkinter import *
from PIL import Image , ImageTk

root = Tk()

root.geometry("1055x844")

#for PNG images
#photo= PhotoImage(file="bg.png")

#for JPG images

image = Image.open("bg.jpg")
photo= ImageTk.PhotoImage(image)
l1=Label(image=photo)
l1.pack()

root.mainloop()