from tkinter import ttk
import tkinter as tk

def extra_opts(root,nb):
    more_set  =ttk.Label(nb)
    nb.add(more_set,text="More Options")
    nb.select(2)
