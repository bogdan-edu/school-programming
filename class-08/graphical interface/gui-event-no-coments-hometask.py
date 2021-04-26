from tkinter import *


def press_btn(event):
    my_text['text'] = 'Молодець, в тебе все вийде!'


root = Tk()
my_text = Label(root, text='Привіт', width=50, height=3)
btn = Button(root, text='Натисни мене')
# Додаємо кнопку
my_btn = Button(root, text='Моя кнопка')
btn.bind('<Button>', press_btn)
my_text.pack()
btn.pack()
my_btn.pack()
root.mainloop()
