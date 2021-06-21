from tkinter import ttk
import tkinter as tk
from common_fns import *
from add_ons import*

def comparison():
    print("DONT LEL PLOX")

def more_opt():
    o = mo.get()
    if o==False:
        fdestroyer(analmf,2)

    if o==True:
        print("More Options to be added!")
        extra_opts(r,nbook)
        






def more_options(event):
    # entry['state']=DISABLED
    fdestroyer(analmf,1)
    a = entry.get()
    print(s," Name: ",a)

    global mo
    mo = tk.BooleanVar(value=False)
    more_opns = ttk.Checkbutton(analmf, text="More Options?",variable=mo,command=more_opt)
    # more_opns.grid(padx= 1,row=4,column=0,sticky = "nsew")
    more_opns.pack(pady=25,padx=20)

    




def check_name(event):
    print("Checking..")
    
    n = entry.get()
    n = n.upper()
    print(n)
    poss = []
    for j in entity_list:
        if (n in j) and (j.index(n)==0 or j[j.index(n)-1]==" "):
            poss.append(j)
            i = entity_list.index(j)
    entry['values']=poss
    entry.event_generate('<Down>')
    # entry.focus()


def name_input(value):
    fdestroyer(analmf,0)
    # menu['state']=DISABLED
    global opt
    opt = anal.get()
    global s
    s = opt.split(" ")[0]
    
    name_frame = ttk.LabelFrame(analmf, text=s.upper() +" NAME")
    name_frame.pack(pady=25,padx=20)
    # name_frame.grid(row=3, column=0, padx=(20, 10), pady=10, sticky="nsew")

    name_label = ttk.Label(name_frame, text= "Select the "+s+" Name: ")
    name_label.configure(font='{} 12 {italic}')
    name_label.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
    aindex = [2,8,7]

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
    # print(entity_list)
    r.bind('<Return>',check_name)
    global entry
    ename = tk.StringVar()
    
    entry = ttk.Combobox(name_frame,textvariable=ename,width=25)
    
    # # ename.trace('w',check_name)
    # analmf.minsize(analmf.winfo_width(), analmf.winfo_height())
    
    entry['values']=entity_list
    # filecombo['state']= "readonly"
    entry.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")
    entry.bind('<<ComboboxSelected>>',more_options)

    



def analysis(root,nb,f):
    # filecombo['state']=DISABLED
    # browsebtn['state']=DISABLED
    global r
    r = root
    global analmf
    analmf = ttk.Frame(nb)
    global nbook
    nbook = nb
    nb.add(analmf,text="Analysis Settings")
    nb.select(1)

    global filepath
    filepath = f
    global ent 
    ent = ["Company","Product","Employee"]
    
    
    
    anal_frame = ttk.Labelframe(analmf, text= "ANALYSIS TYPE")
    anal_frame.pack(pady=25,padx=20)
    # anal_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")

    anal_label = ttk.Label(anal_frame, text= "Choose the type of analysis: ")
    anal_label.configure(font='{} 12 {italic}')
    anal_label.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")


    global anal 
    anal = tk.StringVar()

    anal_opt = ["Company Based Analysis","Product Based Analysis","Employee Based Analysis"]
    
    global menu
    menu = ttk.OptionMenu(anal_frame, anal,"Select Analysis Type",*anal_opt,command=name_input)
    menu.configure(width=30)
    menu.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")

    
