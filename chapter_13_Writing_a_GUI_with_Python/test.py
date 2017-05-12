import tkinter
from tkinter import *

root = Tk()

widget = Label(root)
widget.config(text='My first GUI!!!')
widget.pack(side=TOP, expand=YES, fill=BOTH)
root.mainloop()
