"a simple customizable scrolled listbox component"

from tkinter import *


class ScrolledList(Frame):

    def __init__(self, options, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)                   # make me expandable
        self.makeWidgets(options)

    def handleList(self, event):
        index = self.listbox.curselection()                # on list double-click
        # fetch selection text
        label = self.listbox.get(index)
        # and call action here
        self.runCommand(label)
        # or get(ACTIVE)

    def makeWidgets(self, options):
        sbar = Scrollbar(self)
        list = Listbox(self, relief=SUNKEN)
        # xlink sbar and list
        sbar.config(command=list.yview)
        # move one moves other
        list.config(yscrollcommand=sbar.set)
        # pack first=clip last
        sbar.pack(side=RIGHT, fill=Y)
        list.pack(side=LEFT, expand=YES, fill=BOTH)        # list clipped first
        pos = 0
        for label in options:                              # add to listbox
            # or insert(END,label)
            list.insert(pos, label)
            # or enumerate(options)
            pos += 1
       # list.config(selectmode=SINGLE, setgrid=1)          # select,resize
       # modes
        list.bind('<Double-1>', self.handleList)           # set event handler
        self.listbox = list

    def runCommand(self, selection):                       # redefine me lower
        print('You selected:', selection)

if __name__ == '__main__':
    options = (('Lumberjack-%s' % x)
               for x in range(20))  # or map/lambda, [...]
    ScrolledList(options).mainloop()
