from tkinter import *

root = Tk()
var1 = StringVar()
var2 = StringVar()
check1 = Checkbutton(root, text='One', variable=var1, onvalue='One ON', offvalue='One OFF')
check2 = Checkbutton(root, text='Two', variable=var2, onvalue='Two ON', offvalue='Two OFF')
list_all = Listbox(root, bg='yellow', height=3)


def check_worker(event):
    v1 = var1.get()
    v2 = var2.get()
    l = [v1, v2]
    list_all.delete(0, 1)
    for i in l:
        list_all.insert(END, i)


btn = Button(root, text='Flags value')
btn.bind('<Button-1>', check_worker)
check1.deselect()
check2.deselect()
check1.pack()
check2.pack()
btn.pack()
list_all.pack()
root.mainloop()
