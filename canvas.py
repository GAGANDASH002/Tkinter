from tkinter import *

root=Tk()
canvas_width=800
canvas_height=400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Canvas GUI")

canvas=Canvas(root,width=canvas_width,height=canvas_height)
canvas.pack()

#line goes from point x1,y1 to x2,y2
canvas.create_line(0,0,800,400,fill="red")
canvas.create_line(0,400,800,0,fill="red")

#parameters: coordinate of top left, bottom right
canvas.create_rectangle(3,5,400,700,fill="yellow")

canvas.create_text(200,200,text="python")
canvas.create_oval(344,344,144,144)

canvas.create_arc(4,5,200,200)


root.mainloop()