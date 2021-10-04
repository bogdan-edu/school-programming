from tkinter import *


def printing(event):
    res['text'] = 'Привіт'


root = Tk()

res = Label(root)


button = Button(root)
button['text'] = 'Натиисни мене'
button.bind('<Button>', printing)

res.pack()
button.pack()

root.mainloop()
