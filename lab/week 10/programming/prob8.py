from tkinter import *
import random


def login():
    print("아이디:", e1.get())
    print("패스워드:", e2.get())

def cancel():
    e1.delete(0, END)
    e2.delete(0, END)

window = Tk()
Label(window, text="아이디").grid(row=0, column=0)
Label(window, text="패스워드").grid(row=1, column=0)
e1 = Entry(window)
e2 = Entry(window, show="*")
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
Button(window, text="로그인", command=login).grid(row=2, column=0)
Button(window, text="취소", command=cancel).grid(row=2, column=1)
window.mainloop()
