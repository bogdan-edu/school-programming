from tkinter import *


def printing(event):
    res['text'] = 'Привіт'


root = Tk()

res = Label(root)
res.pack()

button = Button(root)
button['text'] = 'Натиисни мене'
button.bind('<Button>', printing)
button.pack()
root.mainloop()
