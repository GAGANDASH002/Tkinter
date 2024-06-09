from tkinter import *

root= Tk()

def getvals():
    print("It works")

root.geometry("644x344")
l1=Label(root,text="Sardar Travels",font="comicsansms 13 bold",pady=20).grid(column=4)

#text for form
name= Label(root,text="Name")
phone= Label(root,text="Phone")
age= Label(root,text="Age")
pay= Label(root,text="Payment Mode")

#pack text
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
age.grid(row=3,column=2)
pay.grid(row=4,column=2)

#Tkinter variable for storing entries
nameval=StringVar()
phoneval=StringVar()
ageval=StringVar()
payval=StringVar()
foodserviceval=IntVar()#checkbox variable

#Entry for our form
nameentry= Entry(root,textvariable=nameval)
ageentry= Entry(root,textvariable=ageval)
payentry= Entry(root,textvariable=payval)
phoneentry= Entry(root,textvariable=phoneval)

#packing the entry
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
ageentry.grid(row=3,column=3)
payentry.grid(row=4,column=3)

#checkbox
foodservice=Checkbutton(root,text="Want to prebook meals?",variable=foodserviceval)
foodservice.grid(row=6,column=3,pady=10)

#button creation,packing and assigning command
b1= Button(root,text="Submit to Sardar Travels",command=getvals).grid(row=7,column=3)

root.mainloop() 