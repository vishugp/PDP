from tkinter import *

def back_fn(top,root):
    top.destroy()
    root.deiconify()
    # btn_fnl.config(state = wutstate)

def new_window(title,geom):
    window = Toplevel()
    print(title)
    window.title(title)
    window.geometry(geom)
    return window

