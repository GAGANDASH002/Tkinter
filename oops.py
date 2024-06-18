from tkinter import *

class GUI(Tk):#Class GUI inherited from class Tk()
    #constructor
    def __init__(self):
        super().__init__()
        self.geometry("455x355")
    
    def status(self):
        self.var=StringVar()
        self.var.set("Ready")
        self.statusbar=Label(self,textvariable=self.var,relief=SUNKEN,anchor="w")
        self.statusbar.pack(side=BOTTOM,fill=X)
    
    def click(self):
        print("Button Clicked")

    def createButton(self,text):
        Button(text=text,command=self.click).pack()

#main method
if __name__ == '__main__':
    window=GUI()#object of GUI class
    window.status()
    window.createButton("Click Me")
    window.mainloop()