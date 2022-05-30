from tkinter import *
import random, time
def bros():
    x = random.choice(['b.gif','b2.gif','b3.gif',
                       'b4.gif','b5.gif','b6.gif'])
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
root.title('Игра в кости. Сделай бросок')
root.resizable(height = False, width = False)
root.iconphoto(True, PhotoImage(file= ('iconka2.gif')))
font = PhotoImage(file= ('back.gif'))
Label(root, image = font).pack()
lab1 = Label(root)
lab1.place(relx=0.3, rely=0.5, anchor = CENTER)
lab2 = Label(root)
lab2.place(relx=0.7, rely=0.5, anchor = CENTER)
root.bind('<1>', img)
img('event')
root.mainloop()
