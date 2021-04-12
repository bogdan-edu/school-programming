from tkinter import *

root = Tk()
var_a = DoubleVar()
var_b = DoubleVar()
var_c = IntVar()

ent_a = Entry(root, text=var_a)
ent_b = Entry(root, text=var_b)
ent_c = Entry(root, text=var_c)

res = Label(root)


def summary(event):
    a = var_a.get()
    b = var_b.get()
    c = var_c.get()
    res['text'] = '(a + b) / c = ' + str((a + b) / c)


button = Button(root)
button['text'] = 'Додавання'
button.bind('<Button>', summary)

res.pack()
ent_a.pack()
ent_b.pack()
ent_c.pack()
button.pack()

root.mainloop()
