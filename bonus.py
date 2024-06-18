from tkinter import *

root=Tk()
root.geometry("455x355")
root.title("Some tips and tricks of Tkinter")
#root.wm_iconbitmap()#used to change Tkinter icon on GUI window

root.configure(background="grey")#configure the GUI window

width=root.winfo_screenwidth()#obtains width
height=root.winfo_screenheight()#obtains height
print(f'{width}x{height}')

Button(root,text="Close",command=root.destroy).pack()#closes the GUI window

root.mainloop()