from tkinter import *

root = Tk()
var_a = DoubleVar()
var_b = DoubleVar()

ent_a = Entry(root, width=40, bd=5, font='Hack', text=var_a)
ent_b = Entry(root, width=40, bd=5, font='Hack', text=var_b)

res = Label(root, height=2, width=40, font='Hack', border=5)
label_a = Label(root, text='a = ')
label_b = Label(root, text='b = ')


def summary(event):
    a = var_a.get()
    b = var_b.get()
    res['text'] = 'a + b' + str(a + b)


button = Button(root, width=40, height=2, font='Hack', border=5)
button['text'] = 'Додавання'
button.bind('<Button>', summary)
res.pack()
label_a.pack()
ent_a.pack()
label_b.pack()
ent_b.pack()
button.pack()
root.mainloop()
