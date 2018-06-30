from tkinter import *

from p09_isbn import m02_isbn

window = Tk()

window.title("ISBN Prüfung")

window.geometry('350x200')

lbl = Label(window, text="ISBN")

lbl.grid(column=0, row=0)

lbl2 = Label(window, text="")

lbl2.grid(column=1, row=1)

txt = Entry(window, width=10)

txt.grid(column=1, row=0)


def clicked():

    isbn = txt.get()

    check = m02_isbn.verify(isbn)

    if check is True:
        res = txt.get() + " ist gültig"
    else:
        res = txt.get() + " ist ungültig"

    lbl2.configure(text=res)


btn = Button(window, text="Start", command=clicked)

btn.grid(column=2, row=0)

window.mainloop()