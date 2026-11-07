from tkinter.constants import DISABLED
from common_fns import database_maker, fdestroyer
import tkinter as tk
from tkinter import Entry, ttk
from tkinter import filedialog
from tkinter import messagebox
import os


def comparison():
    print("DONT LEL PLOX")

def more_opt():
    o = mo.get()
    if o==False:
        fdestroyer(root,3)

    if o==True:
        print("More Options to be added!")

        more_frame = ttk.LabelFrame(root,text="More Options")
        more_frame.grid(row=5,column=0)
        comp = tk.BooleanVar(value=False)
        compare = ttk.Checkbutton(more_frame, text="Compare between 2 "+s+"'s ?", variable=comp, command=lambda:comparison())
        compare.grid(padx= 1,row=0,column=0,sticky = "nsew")






def more_options(event):
    # entry['state']=DISABLED
    a = entry.get()
    print(s," Name: ",a)

    global mo
    mo = tk.BooleanVar(value=False)
    more_opns = ttk.Checkbutton(root, text="More Options?",variable=mo,command=more_opt)
    more_opns.grid(padx= 1,row=4,column=0,sticky = "nsew")

    




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
    # menu['state']=DISABLED
    global opt
    opt = anal.get()
    global s
    s = opt.split(" ")[0]
    
    name_frame = ttk.LabelFrame(root, text=s.upper() +" NAME")
    # name_frame.pack(fill='x',padx=(20, 20), pady=(20, 10))
    name_frame.grid(row=3, column=0, padx=(20, 10), pady=10, sticky="nsew")

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
    root.bind('<Return>',check_name)
    global entry
    ename = tk.StringVar()
    
    entry = ttk.Combobox(name_frame,textvariable=ename,width=25)
    
    # ename.trace('w',check_name)
    root.minsize(root.winfo_width(), root.winfo_height())
    
    entry['values']=entity_list
    # filecombo['state']= "readonly"
    entry.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")
    entry.bind('<<ComboboxSelected>>',more_options)

    



def analysis():
    # filecombo['state']=DISABLED
    # browsebtn['state']=DISABLED
    

    
    fdestroyer(root,2)
    
    anal_frame = ttk.Labelframe(root, text= "ANALYSIS TYPE")
    # anal_frame.pack(fill='x',padx=(20, 20), pady=(20, 10))
    anal_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")

    anal_label = ttk.Label(anal_frame, text= "Choose the type of analysis: ")
    anal_label.configure(font='{} 12 {italic}')
    anal_label.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")


    global anal 
    anal = tk.StringVar()

    anal_opt = ["Company Based Analysis","Product Based Analysis","Employee Based Analysis"]
    
    global menu
    menu = ttk.OptionMenu(anal_frame, anal,"Select Analysis Type",*anal_opt,command=name_input)
    menu.configure(width=20)
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
root  = tk.Tk()
root.title("PDP SALES ANALYSIS PLATFORM")
root.option_add("*tearOff", False) 

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



## MAIN PAGE 
welcome = ttk.Label(root, text="Welcome to PDP Sales Analysis!",foreground="#007fff")
welcome.configure(font='{} 21 {bold underline}')
# welcome.pack(pady=10)
welcome.grid(row=0, column=0)




fileframe = ttk.LabelFrame(root, text="DATABASE FILEPATH", padding=(20,10))
# fileframe.pack(fill='x',padx=(20, 20), pady=(20, 10))
fileframe.grid(row=1, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

# File Location Label
dbsel = ttk.Label(fileframe, text= "Enter Database fileframe: ")
dbsel.configure(font='{azure} 12 {italic}')
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
fdestroyer(root,1)


# Center the window, and set minsize
root.update()
print(root.winfo_width(),root.winfo_height())
root.minsize(root.winfo_width(),root.winfo_height())
x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

# Start the main loop
root.mainloop()

