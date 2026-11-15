from tkinter import *
import random


size = 100

def left_click(event):
    global size
    size = size + 10
    canvas.delete("all")
    canvas.create_rectangle(200 - size, 150 - size, 200 + size, 150 + size)

def right_click(event):
    global size
    size = size - 10
    canvas.delete("all")
    canvas.create_rectangle(200 - size, 150 - size, 200 + size, 150 + size)

window = Tk()
canvas = Canvas(window, width=400, height=300)
canvas.pack()
canvas.create_rectangle(100, 50, 300, 250)
canvas.bind("<Button-1>", left_click)
canvas.bind("<Button-3>", right_click)
window.mainloop()
