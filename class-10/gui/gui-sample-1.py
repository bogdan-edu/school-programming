
from tkinter import *


def summary(e):
    a = int(input('a = '))
    b = int(input('b = '))
    print(' a + b = ', a + b)


root = Tk()
button = Button(root)
button['text'] = 'Додавання'
button.bind('<Button>', summary)
button.pack()
root.mainloop()

