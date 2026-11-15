from tkinter import *
import random


window = Tk()
canvas = Canvas(window, width=500, height=400)
canvas.pack()
color = ["red", "orange", "yellow", "green", "blue", "violet"]
for i in range(10):
    x1 = random.randint(0, 400)
    y1 = random.randint(0, 300)
    x2 = x1 + random.randint(20, 300)
    y2 = y1 + random.randint(20, 300)
    fill_color = random.choice(color)
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)
window.mainloop()
