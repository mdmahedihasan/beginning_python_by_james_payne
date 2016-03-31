import tkinter
from tkinter import *

state = ''
buttons = []


def choose(i):
    global state
    state = i
    for btn in buttons:
        btn.deselect()
    buttons[i].select()


root = Tk()
for i in range(4):
    radio = Radiobutton(root, text=str(i), value=str(i), command=(lambda i=i: choose(i)))
    radio.pack(side=BOTTOM)
    buttons.append(radio)

root.mainloop()
print('You choose the following number : ', state)
