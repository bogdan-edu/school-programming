from tkinter import *


def summary(event):
    a = int(input('a = '))
    b = int(input('b = '))
    print(' a + b = ', a + b)


def hello(event):
    print('Привіт, я твоя перша програма з графічним інтерфейсом')


root = Tk()

button = Button(root)
button['text'] = 'Додавання'
button.bind('<Button>', summary)
button.pack()

button_hello = Button(root)
button_hello['text'] = 'Вітання'
button_hello.bind('<Button>', hello)
button_hello.pack()

root.mainloop()
