from tkinter import *
import random


def key(event):
    if event.keysym == "Left":
        canvas.move(rect, -10, 0)
    elif event.keysym == "Right":
        canvas.move(rect, 10, 0)
    elif event.keysym == "Up":
        canvas.move(rect, 0, -10)
    elif event.keysym == "Down":
        canvas.move(rect, 0, 10)

window = Tk()
canvas = Canvas(window, width=500, height=300)
canvas.pack()
rect = canvas.create_rectangle(10, 200, 60, 260, fill="green")
window.bind("<Key>", key)
window.mainloop()
