gifdir = "E:\\workspace\\PP4E-Examples-1.2\\Examples\\PP4E\\Gui\\gifs\\"
from tkinter import *
win = Tk()
igm = PhotoImage(file=gifdir + "ora-pp.gif")
Button(win, image=igm).pack()
win.mainloop()
