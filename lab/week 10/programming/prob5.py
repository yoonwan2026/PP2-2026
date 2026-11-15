from tkinter import *
import random


total = 0

def minus():
    global total
    total = total - 1
    label['text'] = str(total)

def plus():
    global total
    total = total + 1
    label['text'] = str(total)

window = Tk()
b1 = Button(window, text="감소", width=10, command=minus)
label = Label(window, text="0", width=10)
b2 = Button(window, text="증가", width=10, command=plus)
b1.pack(side=LEFT)
label.pack(side=LEFT)
b2.pack(side=LEFT)
window.mainloop()
