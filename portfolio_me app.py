from tkinter import *

class Resume:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x500')
        self.root.title('My Resume')
        d = {'Name': 'Deep Pati', 'Address': 'Raniganj', 'Contact No': '9749606170'}
        x = 0
        for i in d:
            Label(self.root, text=i, font=('arial', 20), padx=10, pady=10).grid(row=x, column=0, sticky='NE')
            Label(self.root, text=':', font=('arial', 20), padx=10, pady=10).grid(row=x, column=1)
            Label(self.root, text=d[i], font=('arial', 20), padx=10, pady=10).grid(row=x, column=2, sticky='NW')
            x += 1
        self.root.mainloop()

# main
obj = Resume()