from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()
root.geometry("455x233")
root.title("Slider in Tkinter")

def getdollar():
    print(f"Dollars credited:{myslider2.get()}")
    tmsg.showinfo("Amount Credited",f"We have credited {myslider2.get()} dollars into your account")

#myslider = Scale(root,from_=0, to=455)
#myslider.pack()
Label(root,text="How many dollars needed?").pack()
myslider2 = Scale(root,from_=0, to=100,orient=HORIZONTAL,tickinterval=50)
myslider2.set(35)
myslider2.pack()
Button(root,text="Get $",command=getdollar).pack()
root.mainloop()