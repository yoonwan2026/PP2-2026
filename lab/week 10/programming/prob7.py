from tkinter import *
import random


def convert():
    inch_val = float(entry.get())
    cm = inch_val * 2.54
    result['text'] = str(cm) + " 센티미터"

window = Tk()
Label(window, text="인치를 입력하시오:").grid(row=0, column=0)
Label(window, text="변환결과:").grid(row=1, column=0)
entry = Entry(window)
entry.grid(row=0, column=1)
result = Label(window, text="")
result.grid(row=1, column=1)
Button(window, text="변환!", command=convert).grid(row=2, column=1)
window.mainloop()
