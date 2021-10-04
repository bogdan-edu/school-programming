from tkinter import *


def press_btn(event):
    my_text['text'] = 'Молодець, в тебе все вийде!'


# Додаємо функцію обробник для другої кнопки
def my_function(event):
    my_text['text'] = 'Молодець, в тебе все вийшло!'


root = Tk()
my_text = Label(root, text='Привіт', width=50, height=3)
btn = Button(root, text='Натисни мене')
# Додаємо кнопку
my_btn = Button(root, text='Моя кнопка')
btn.bind('<Button>', press_btn)
# Пов'язуємо обробник my_function з подією натискання нової кнопки
my_btn.bind('<Button>', my_function)
my_text.pack()
btn.pack()
# Застосовуємо метод pack до нової кнопки
my_btn.pack()
root.mainloop()
