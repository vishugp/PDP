# Time Based Analysis
from tkinter import *
from common_fns import *

def time_based(layer,loc):
    print("Time Based Analysis")

def time_window(top,root):
  root.withdraw()
  top.resizable(0,0)
  label = Label(top, text="TBA").pack()
  # root.deiconify()

  backbtn = Button(top, text="<==", command=lambda: back_fn(top,root))
  backbtn.place(anchor='nw', width='50', x='0', y='0')
  top.protocol("WM_DELETE_WINDOW",root.destroy)