from tkinter import ttk
import tkinter as tk
from common_fns import *

def extra_opts(root,nb,filepath,ent,aindex,s,a):
    more_set  =ttk.Label(nb)
    nb.add(more_set,text="More Options")
    nb.select(2)

    # #getting screen width and height of display
    # width= root.winfo_screenwidth() 
    # height= root.winfo_screenheight()
    # #setting tkinter root size
    # root.geometry("%dx%d" % (width, height))

    global pdf
    pdp = database_maker(filepath,aindex[ent.index(s)])

    global entity_list
    entity_list = list()
    global count_list
    count_list = list()
    global keys
    keys = list()
    global names
    names = []

    for i in range(int(pdp[0][0][0])):
        entity_list.append(pdp[i][0][1])
        count_list.append(int(pdp[i][0][2]))
    
    for i in pdp[0][1]:
        keys.append(i)