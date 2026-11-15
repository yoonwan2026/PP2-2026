from tkinter import *
import random


def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)

def submit():
    print(e1.get(), e2.get(), e3.get(), e4.get(), e5.get())

window = Tk()
Label(window, text="이름").grid(row=0, column=0)
Label(window, text="주소").grid(row=1, column=0)
Label(window, text="시").grid(row=2, column=0)
Label(window, text="우편번호").grid(row=3, column=0)
Label(window, text="국가").grid(row=4, column=0)
e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window)
e4 = Entry(window)
e5 = Entry(window)
e1.grid(row=0, column=1, sticky=W+E)
e2.grid(row=1, column=1, sticky=W+E)
e3.grid(row=2, column=1, sticky=W+E)
e4.grid(row=3, column=1, sticky=W+E)
e5.grid(row=4, column=1, sticky=W+E)
window.columnconfigure(1, weight=1)
Button(window, text="Clear", command=clear).grid(row=5, column=1, sticky=E)
Button(window, text="Submit", command=submit).grid(row=5, column=2)
window.mainloop()
