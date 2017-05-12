import tkinter
from tkinter import *

root = Tk()
labelFont = ('times', 24, 'italic')

widget = Label(root, text='Eat as JOES')
widget.config(bg='black', fg='red')
widget.pack(expand=YES, fill=BOTH)

root.mainloop()
