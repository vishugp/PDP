from analysis_settings import analysis
from tkinter.constants import DISABLED
from common_fns import database_maker, fdestroyer
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import Entry, PhotoImage, ttk
from tkinter import filedialog
from tkinter import messagebox
import os



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
        analysis(root,notebook,filepath)
        
        
        
        

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


# Center the window, and set minsize
root.update()
print(root.winfo_width(),root.winfo_height())
root.minsize(root.winfo_width(),root.winfo_height())
x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

root.mainloop()