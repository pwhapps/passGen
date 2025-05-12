from tkinter import *
from main import final_password

root = Tk()

root.title("Password Generator")

root.geometry('250x100')


def clicked():  # runs main.py on generate button click.
    result = final_password()
    text = my_box.config(text=result)
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    return text


def copy():  # copies text to clipboard.
    root.clipboard_clear()
    root.clipboard_append(my_box.cget('text'))


def clear():
    my_box.config(text='')
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)


# defines label where password is displayed.
my_box = Label(root, text='')
my_box.pack(side='top', pady=20)

# defines button properties.
btn = Button(root, text='Generate', command=clicked)

btn1 = Button(root, text='Copy', command=copy, state=DISABLED)

btn2 = Button(root, text='Clear', command=clear, state=DISABLED)

btn.pack(side='left', padx=5, pady=5)
btn1.pack(side='left', padx=5, pady=5)
btn2.pack(side='left', padx=5, pady=5)
root.mainloop()
