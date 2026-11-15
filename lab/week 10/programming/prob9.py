from tkinter import *
import random


def show():
    print("이름:", e1.get())
    print("직업:", e2.get())
    print("국적:", e3.get())

window = Tk()
Label(window, text="이름").grid(row=0, column=0)
Label(window, text="직업").grid(row=1, column=0)
Label(window, text="국적").grid(row=2, column=0)
e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
Button(window, text="Show", command=show).grid(row=3, column=0)
Button(window, text="Quit", command=window.destroy).grid(row=3, column=1)
window.mainloop()
