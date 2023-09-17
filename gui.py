from tkinter import *
from main import RandomPass

root = Tk()

root.title("Password Generator")

root.geometry('250x100')


def clicked():  # runs main.py on generate button click.
    result = RandomPass().final_password()
    text = my_box.config(text=result)
    return text


def copy():  # copies text to clipboard.
    root.clipboard_clear()
    root.clipboard_append(my_box.cget('text'))


# Defines label where password is displayed.
my_box = Label(root, text='')
my_box.pack()


btn = Button(root, text='Generate', command=clicked)
btn1 = Button(root, text='Copy', command=copy)

btn.pack(side='top')
btn1.pack()
root.mainloop()
