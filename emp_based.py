# Employee Based Analysis
from common_fns import *
from tkinter import *

def emp_based(layer,loc):
    print("Employee Based Analysis")

def emp_window(top,root):
  root.withdraw()
  top.resizable(0,0)
  label = Label(top, text="EBA").pack()
  # root.deiconify()

  backbtn = Button(top, text="<==", command=lambda: back_fn(top,root))
  backbtn.place(anchor='nw', width='50', x='0', y='0')
  top.protocol("WM_DELETE_WINDOW",root.destroy)