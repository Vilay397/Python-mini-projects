import random
import time
from tkinter import *


def bros():
    x = random.choice(['image/b.gif', 'image/b2.gif', 'image/b3.gif',
                       'image/b4.gif', 'image/b5.gif', 'image/b6.gif'])
    return x
def img(event):
    global b1, b2
    for i in range(18):
        b1 = PhotoImage(file=(bros()))
        b2 = PhotoImage(file=(bros()))
        lab1['image'] = b1
        lab2['image'] = b2
        root.update()
        time.sleep(0.12)


root = Tk()
root.geometry('600x400')
root.title('Game in dice. Go...')
root.resizable(height=False, width=False)
root.iconphoto(True, PhotoImage(file=('image/iconka2.gif')))
font = PhotoImage(file=('image/back.gif'))
Label(root, image=font).pack()
lab1 = Label(root)
lab1.place(relx=0.3, rely=0.5, anchor=CENTER)
lab2 = Label(root)
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)
root.bind('<1>', img)
img('event')
root.mainloop()
