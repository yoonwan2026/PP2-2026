from tkinter import *
import random


def roll():
    n = random.randint(1, 6)
    label['text'] = str(n)

window = Tk()
label = Label(window, text="0", width=10)
label.pack(side=LEFT)
button = Button(window, text="굴리기", command=roll)
button.pack(side=LEFT)
window.mainloop()
