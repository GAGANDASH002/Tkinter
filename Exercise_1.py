#creating a NewsPaper GUI

from tkinter import *
from PIL import Image,ImageTk

def every_100(text):
    final_text=""
    for i in range(0,len(text)):
        final_text+=text[i]
        if i%100==0 and i!=0:
            final_text+="\n"
    return final_text 
    
root=Tk()
root.title("The Daily")

root.geometry("1000x1000")

texts=[]
photos=[]
for i in range(0,3):
    with open(f"{i+1}.txt") as f:
        text=f.read()
        texts.append(every_100(text))

    image=  Image.open(f"{i+1}.png")
    #resize these images
    image=image.resize((323,165))

    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root,width=800,height=70)
Label(f0,text="The Daily Samachar",font="lucida 30 bold").pack()
Label(f0,text="June 07 2024",font="lucida 20 bold").pack()
f0.pack()


f1= Frame(root,width=900,height=200,pady=14)
Label(f1,text=texts[0]).pack(side=LEFT,padx=20,pady=20)
Label(f1,image=photos[0],anchor="e").pack()
f1.pack(anchor="w")

f2= Frame(root,width=900,height=200,pady=14)
Label(f2,text=texts[1]).pack(side=RIGHT,padx=20,pady=20)
Label(f2,image=photos[1],anchor="e").pack()
f2.pack(anchor="w")

f3= Frame(root,width=900,height=200,pady=14)
Label(f3,text=texts[2]).pack(side=LEFT,padx=20,pady=20)
Label(f3,image=photos[2],anchor="e").pack()
f3.pack(anchor="w")

root.mainloop()