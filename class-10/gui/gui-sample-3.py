from tkinter import *

root = Tk()
var_a = DoubleVar()
var_b = DoubleVar()

ent_a = Entry(root, width=20, bd=3, text=var_a)
ent_b = Entry(root, width=20, bd=3, text=var_b)

res = Label(root)


def summary(event):
    a = var_a.get()
    b = var_b.get()
    res['text'] = str(a + b)


button = Button(root)
button['text'] = 'Додавання'
button.bind('<Button>', summary)
ent_a.pack()
ent_b.pack()
res.pack()
button.pack()
root.mainloop()
