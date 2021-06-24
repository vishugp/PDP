from analysis_settings import analysis
from tkinter.constants import DISABLED
from common_fns import database_maker, fdestroyer
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import Entry, PhotoImage, ttk
from tkinter import filedialog
from tkinter import messagebox
import os
from common_fns import *
import math

def results():
    print("RESULTS")
    resf = ttk.Frame(notebook)
    notebook.add(resf,text="Analysis Results")
    notebook.select(len(notebook.winfo_children())-1)
    # print(notebook.winfo_children())
    # notebook.select('Analysis Results')


    resnb = ttk.Notebook(resf)
    resnb.pack(expand=True, fill="both", padx=5, pady=5)

    sheet = ttk.Frame(resnb)
    sheet.pack(expand=True, fill="both", padx=5, pady=5)

    namalab = ttk.Label(sheet, text=s +" Name: "+nama)
    namalab.pack()
    
    resnb.add(sheet,text="All Sales")
    
    treescroll = ttk.Scrollbar(sheet)
    tree = ttk.Treeview(sheet, yscrollcommand=treescroll.set)
    treescroll.config(command=tree.yview)

    indices = [8,3,5,6,9,1,7]
    collist = list()
    for i in range(len(indices)):
        collist.append(i+1)
    tree["columns"] = collist
    tree["show"] = 'headings'

    nindex = entity_list.index(nama)
    for i in range(len(indices)):
        tree.column(i+1, width = math.floor(root.winfo_width()/len(indices)), anchor = 'c')
        tree.heading(i+1,text = keys[indices[i]])

    c = count_list[nindex]
    print(c)
    for i in range(c):
        row = list()
        for j in range(len(indices)):
            data = pdp[nindex][2+i][indices[j]]
            if indices[j]:
                data = data[:10]    #Time Setting
            row.append(data)
        tree.insert("",'end',values=row)

    
    treescroll.pack(side="right", fill="y")
    tree.pack(expand=True, fill="both")




def extra_opts():
    more_set  =ttk.Label(notebook)
    notebook.add(more_set,text="More Options")
    notebook.select(2)
    res.pack_forget()
    # #getting screen width and height of display
    # width= root.winfo_screenwidth() 
    # height= root.winfo_screenheight()
    # #setting tkinter root size
    # root.geometry("%dx%d" % (width, height))

    res2 = ttk.Button(more_set,text="RESULTS",style="AccentButton",command=lambda: results())
    res2.pack()

def more_opt():
    o = mo.get()
    if o==False:
        fdestroyer(notebook,1)
        res.pack()

    if o==True:
        print("More Options to be added!")
        extra_opts()


def more_options(event):
    # entry['state']=DISABLED
    fdestroyer(analmf,1)
    global nama
    nama = entry.get()
    print(s," Name: ",nama)

    global mo
    mo = tk.BooleanVar(value=False)
    more_opns = ttk.Checkbutton(analmf, text="More Options?",variable=mo,command=more_opt)
    # more_opns.grid(padx= 1,row=4,column=0,sticky = "nsew")
    more_opns.pack(pady=25,padx=20)

    global res
    res = ttk.Button(analmf, text = "RESULTS", style="AccentButton",command=lambda:results())
    res.pack(pady=20)

    root.minsize(root.winfo_width(), root.winfo_height())
    root.update()

    




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
    name_label.configure(font='{} 13 {italic}')
    name_label.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
    global aindex
    aindex = [2,8,7]

    global pdp
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
    root.bind('<Return>',check_name)
    global entry
    ename = tk.StringVar()
    
    entry = ttk.Combobox(name_frame,textvariable=ename,width=25)
    
    # # ename.trace('w',check_name)
    # analmf.minsize(analmf.winfo_width(), analmf.winfo_height())
    
    entry['values']=entity_list
    # filecombo['state']= "readonly"
    entry.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")
    entry.bind('<<ComboboxSelected>>',more_options)

    



def analysis():
    # filecombo['state']=DISABLED
    # browsebtn['state']=DISABLED
    global analmf
    analmf = ttk.Frame(notebook)
    notebook.add(analmf,text="Analysis Settings")
    notebook.select(1)
    
    anal_frame = ttk.Labelframe(analmf, text= "ANALYSIS TYPE")
    anal_frame.pack(pady=25,padx=20)
    # anal_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")

    anal_label = ttk.Label(anal_frame, text= "Choose the type of analysis: ")
    anal_label.configure(font='{} 13 {italic}')
    anal_label.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")


    global anal 
    anal = tk.StringVar()

    anal_opt = ["Company Based Analysis","Product Based Analysis","Employee Based Analysis"]
    
    global menu
    menu = ttk.OptionMenu(anal_frame, anal,"Select Analysis Type",*anal_opt,command=name_input)
    menu.configure(width=30)
    menu.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")

    

    


def check_xlsx(index, value, op):
    # print("Checking the Database File...")
    c = filecombo.get()
    global filepath
    if c=="":
        filepath = "No File Selected"
    elif c[0]=="/":
        filepath = c
    else:
        filepath = filedir + c


    if filepath[-4:] != "xlsx":
        messagebox.showerror("Invalid file Format","Please provide database file with '.xlsx' file format!")
        filecombo.set("")
    else:
        fdestroyer(notebook,0)
        analysis()
        
        
        
        

def dbselect(filecombo):
    root.filename = filedialog.askopenfilename(initialdir="/home/vishu/",
                                            title = "Select the database file",
                                            )
    
    # filecombo.delete('0', 'end')
    # filecombo.insert('0', root.filename)
    if root.filename not in filecombo['values']:
        filecombo['values']+= (root.filename,)
        filecombo.current(len(filecombo['values'])-1)
    else:
        filecombo.current(filecombo['values'].index(root.filename))



global root
root=tk.Tk()
root.title("PDP SALES ANALYSIS")
root.option_add("*tearOff", False) 
pic = PhotoImage(file = 'pdplogo.png')
# root.iconbitmap(r'pdplogo.ico')
root.iconphoto(False, pic)



# Make the app responsive
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)

# STYLE
styleloc = os.path.abspath(os.getcwd()) + "/Azure-ttk-theme/azure.tcl"
# print(styleloc)
root.tk.call("source", styleloc)
style = ttk.Style(root)
style.theme_use("azure")

global notebook
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", padx=5, pady=5)

home=ttk.Frame(notebook)
notebook.add(home, text="Home")

title = ttk.Label(home, text="PDP SALES ANALYSIS",foreground="#007fff")
title.configure(font='{} 21 {bold underline}')
# title.grid(row=0, column=0,pady=20)
title.pack(pady=50)


fileframe = ttk.LabelFrame(home, text="DATABASE FILEPATH", padding=(20,10))
# fileframe.pack(fill='x',padx=(20, 20), pady=(20, 10))
# fileframe.grid(row=1, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")
fileframe.pack(pady=25,padx=20)

# File Location Label
dbsel = ttk.Label(fileframe, text= "Enter Database fileframe: ")
dbsel.configure(font='{azure} 13 {italic}')
dbsel.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
# dbsel.pack(side='left',padx=100,pady=10)


global ent 
ent = ["Company","Product","Employee"]
global filedir
filedir = os.path.abspath(os.getcwd())
filedir=filedir[:-12]
filedir+="Downloads/"
filelist = os.listdir(filedir)
finallist = []
for i in filelist:
    if i[-4:] == "xlsx":
        finallist.append(i)
        # print(i)
finallist.sort()

global filecombo
global fname
fname = tk.StringVar()
fname.trace('w',check_xlsx)
filecombo = ttk.Combobox(fileframe,textvariable=fname,width=50)
filecombo['values']=finallist
filecombo['state']= "readonly"
filecombo.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")
# filecombo.pack(side='left',padx=25,pady=10)
# filecombo.bind('<<ComboboxSelected>>',check_xlsx)

browsebtn = ttk.Button(fileframe, text="BROWSE",command=lambda: dbselect(filecombo),style="AccentButton")
browsebtn.grid(row=0, column=2, padx=5, pady=10, sticky="nsew")
# browsebtn.pack(side='left',padx=20,pady=10)


# Center the window, and set minsize
root.update()
print(root.winfo_width(),root.winfo_height())
root.minsize(root.winfo_width(),root.winfo_height())
x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

root.mainloop()