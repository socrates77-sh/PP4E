"""
4 demo class components (subframes) on one window;
there are 5 Quitter buttons on this one window too, and each kills entire gui;
GUIs can be reused as frames in container, independent windows, or processes;
"""

from tkinter import *
from quitter import Quitter
demoModules = ['demoDlg', 'demoCheck', 'demoRadio', 'demoScale']
parts = []


def addComponents(root):
    for demo in demoModules:
        module = __import__(demo)                       # import by name string
        # attach, config instance
        part = module.Demo(root, bd=6, relief=RIDGE)
        # part.config(bd=2, relief=GROOVE)               # config when created
        # grow, stretch with window
        part.pack(side=LEFT, expand=YES, fill=BOTH)
        parts.append(part)                              # change list in-place


def dumpState():
    for part in parts:                                  # run demo report if any
        print(part.__module__ + ':', end=' ')
        if hasattr(part, 'report'):
            part.report()
        else:
            print('none')

root = Tk()                                             # make explicit root first
root.title('Frames')
Label(root, text='Multiple Frame demo', bg='white').pack()
Button(root, text='States', command=dumpState).pack(fill=X)
Quitter(root).pack(fill=X)
addComponents(root)
root.mainloop()
