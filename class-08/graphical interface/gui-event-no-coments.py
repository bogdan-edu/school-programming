from tkinter import *


def press_btn(event):
    my_text['text'] = 'Молодець, в тебе все вийде!'


root = Tk()
my_text = Label(root, text='Привіт', width=50, height=3)
btn = Button(root, text='Натисни мене')
btn.bind('<Button>', press_btn)
my_text.pack()
btn.pack()
root.mainloop()
