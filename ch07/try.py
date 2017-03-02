import sys
from tkinter import *                        # lambda generates a function


def func(str):
    print(str)

widget = Button(None,                        # but contains just an expression
                text='Hello event world',
                # command=(lambda: func('aaa')))
                command=func('aaa'))

widget.pack()
widget.mainloop()
