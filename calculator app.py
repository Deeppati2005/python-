import tkinter
from tkinter import *


class calc:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x300')
        self.root.title('A Simple Calculator')
        L = ['First Number', 'Second Number', 'Result']
        x = 0
        for i in L:
            Label(self.root, text=i, font=('verdana', 20), padx=10,
                  pady=10).grid(row=x, column=0, sticky='NE')
            x += 1
        self.t1 = Entry()
        self.t1.grid(row=0, column=1, padx=10, pady=10)

        self.t2 = Entry()
        self.t2.grid(row=1, column=1, padx=10, pady=10)

        self.t3 = Entry()
        self.t3.grid(row=2, column=1, padx=10, pady=10)

        self.b1 = Button(self.root, text='+',
                         font=('verdana', 20), command=self.sum)
        self.b1.grid(row=3, column=0)
        self.root.mainloop()

    def sum(self):
        a = int(self.t1.get())
        b = int(self.t2.get())
        c = a+b
        self.t3.insert(0, c)


obj = calc()
