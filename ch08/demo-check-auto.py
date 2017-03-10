# check buttons, the easy way

from tkinter import *
root = Tk()
states = []
for i in range(10):
    var = IntVar()
    chk = Checkbutton(root, text=str(i), variable=var)
    chk.pack(side=LEFT)
    states.append(var)
root.mainloop()                               # let tkinter keep track
# show all states on exit (or map/lambda)
print([var.get() for var in states])


# alternatives
# print(list(map(IntVar.get, states)))
# print(list(map(lambda var: var.get(), states)))
