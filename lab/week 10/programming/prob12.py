from tkinter import *
import random


def go_left():
    canvas.move(rect, -10, 0)

def go_right():
    canvas.move(rect, 10, 0)

def go_up():
    canvas.move(rect, 0, -10)

def go_down():
    canvas.move(rect, 0, 10)

window = Tk()
canvas = Canvas(window, width=500, height=400)
canvas.pack()
rect = canvas.create_rectangle(200, 150, 300, 250, fill="red")
Button(window, text="<-(left)", command=go_left).pack(side=LEFT)
Button(window, text="->(right)", command=go_right).pack(side=LEFT)
Button(window, text="^(up)", command=go_up).pack(side=LEFT)
Button(window, text="V(down)", command=go_down).pack(side=LEFT)
window.mainloop()
