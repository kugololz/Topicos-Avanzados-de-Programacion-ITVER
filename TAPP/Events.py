from tkinter import *

def keylisten(event):
    print("he leido una a")


win = Tk()
win.bind("<Key-a>", keylisten)
win.bind("<Key-A>", keylisten)

win.mainloop()