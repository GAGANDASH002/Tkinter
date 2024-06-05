from tkinter import *

root=Tk()
root.geometry("444x233")
root.title("My GUI")

#Important Label Options
'''text= adds the text
bd= background
fg=foreground
font= sets the font    e.g- font=("comicsansms",19,"bold")
padx= padding of X
pady= padding of Y
relief=border-styling - SUNKEN, RAISED,GROOVE,RIDGE'''

title_label= Label(text="""Virat Kohli
                   \nis an Indian international 
                   \ncricketer and the former 
                   \ncaptain of the Indian national cricket team. 
                   \nHe is a right-handed batsman and
                    \nan occasional medium-fast bowler. 
                   \nHe currently represents Royal Challengers Bengaluru in the IPL and Delhi
                 """, bg="red",fg="white",padx=25,pady=50,font="comicsansms 19 bold",borderwidth=3,relief=SUNKEN)

'''IMPORTANT PACK OPTIONS
anchor
side=top,bottom,left,right
fill
padx
pady
'''

title_label.pack(anchor="ne",side=BOTTOM,fill=Y,padx=20,pady=20)
root.mainloop()