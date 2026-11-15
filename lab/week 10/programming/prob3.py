from tkinter import *
import random


window = Tk()
for i in range(3):
    for j in range(10):
        b = Button(window, text=str(i) + "행," + str(j) + "열")
        b.grid(row=i, column=j)
window.mainloop()
