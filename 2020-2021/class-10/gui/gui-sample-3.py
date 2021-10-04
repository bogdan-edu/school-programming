from tkinter import *

root = Tk()
var_a = DoubleVar()
var_b = DoubleVar()

ent_a = Entry(root, width=40, bd=5, font='Hack', text=var_a)
ent_b = Entry(root, width=40, bd=5, font='Hack', text=var_b)

res = Label(root, height=2, width=40, font='Hack', border=5)


def summary(event):
    a = var_a.get()
    b = var_b.get()
    res['text'] = str(a + b)


button = Button(root, width=40, height=2, font='Hack', border=5)
button['text'] = 'Додавання'
button.bind('<Button>', summary)
res.pack()
ent_a.pack()
ent_b.pack()
button.pack()
root.mainloop()
