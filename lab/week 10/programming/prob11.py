from tkinter import *
import random


x = 0

def move_text():
    global x
    x = x + 5
    if x > 400:
        x = 0
    canvas.delete("all")
    canvas.create_text(x, 150, text="파이썬 커피샵으로 오세요!")
    window.after(50, move_text)

window = Tk()
canvas = Canvas(window, width=400, height=300)
canvas.pack()
move_text()
window.mainloop()
