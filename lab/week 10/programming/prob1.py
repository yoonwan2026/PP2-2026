from tkinter import *
import random


def click():
    label['text'] = 'clicked'

window = Tk()
window.title("Welcome to tkinter")
label = Label(window, text='Hi!')
label.pack(side=LEFT)
button = Button(window, text='click me', command=click)
button.pack(side=LEFT)
window.mainloop()
