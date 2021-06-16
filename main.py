from common_fns import *
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
import pandas as pd
import os.path
from os import path
from company_based import *
from product_based import *
from time_based import *
from emp_based import *

basis = ['COMPANY BASED ANALYSIS','PRODUCT BASED ANALYSIS','EMPLOYEE BASED ANALYSIS']
flag1 = 0
w = 800
h = 600
windgeom = str(w) +"x"+ str(h)
# windgeom = "800x600"
root = Tk()
root.title('PDP SALES ANALYSIS')
root.geometry(windgeom)
root.resizable(0,0)
root.filename = ""


def dbselect():
    root.filename = filedialog.askopenfilename(initialdir="/home/vishu/Downloads",
                                            title = "Select the database",
                                            )
    
    fileloctext.delete('0', 'end')
    fileloctext.insert('0', root.filename)

def analysis_opt(k):
    top = new_window(basis[k],windgeom)

    if k==0:
        company_based(top,root)
    elif k==1:
        product_based(top, root)
    elif k==2:
        emp_based(top,root)
    elif k==3:
        time_window(top,root)
        
    root.withdraw()
    analysis.destroy()
    nextbtn.destroy()
    browsebtn.config(state = NORMAL)

def anal():
    global z
    z=88
    for i in analist.curselection():
        z = i
        opt = analist.get(i)
    

    # Selected Option
    # if browsebtn['state']== NORMAL:
        # messagebox.showwarning("Database File Error", "Please Select the Database File!")

    # else: 
    try:
        opt+=" ANALYSIS"
        opt=opt.upper()
    # msgtext = "Database file: \n" + root.filename + "\nAnalysis type: \n" + opt
    # final = messagebox.askyesno("Options?",msgtext)
    # if final == True:
    
    # else:
        # browsebtn.configure(state=NORMAL)

        sel_anal.configure(text=opt)

        selbtn['state']=DISABLED
        global nextbtn
        nextbtn = Button(root, text="NEXT",height=4,width=8,bg="green",fg="white",command= lambda: analysis_opt(z) )
        nextbtn.pack(side=RIGHT,pady=10,padx=10)
    
            
    except:
        messagebox.showinfo("Select Analysis Type","Please Select the type of Analysis to be performed from the given List!")
            

    

def check_file(filenama):
    if filenama=="":
        messagebox.showerror("File not Selected","Please Select Database File")
    
    

    # Entry Box Checker
    elif path.exists(filenama)!=True:
        messagebox.showerror("Invalid File Path","File Path is Incorrect")
        fileloctext.delete('0', 'end')

    else:
        x = filenama.split(".")[-1]
        # print(type(filenama))
        # print(x)
        if x!="xlsx":
            messagebox.showerror("Invalid file Format","Please provide database file with '.xlsx' file format!")
        elif (browsebtn['state']!=DISABLED):
            analysis_list()  
            browsebtn.config(state = DISABLED)



def analysis_list():
    global analysis
    analysis = LabelFrame(root,text="Analysis Type")
    analysis.pack(fill="x",padx = 20)

    # Analysis Option
    opt_anal = Label(analysis, text= "Choose the type of analysis: ")
    opt_anal.configure(font='{} 12 {italic}')
    # opt_anal.place(anchor='w', relx='0.05', rely='0.625', x='0', y='0')
    opt_anal.grid(column=0,row=0,padx=5)

    
    # Analysis Types List
    global analist
    analist = Listbox(analysis,height=3 ,width=25,font = '{} 10 {}', selectmode=BROWSE)
    for i in range(len(basis)):
        analist.insert(i+1,basis[i])
    # analist.place(anchor='n', relx='0.65', rely='0.6', x='0', y='0')
    analist.grid(column=1,row=0,padx=5,pady=5)


    # Next Button
    global selbtn
    selbtn = Button(analysis, text="Select",command = anal)
    # next.place(anchor='nw', height='75', relx='0.73', rely='0.8', width='200', x='0', y='0')
    selbtn.grid(column=2,row=0,padx=10)

    # Selected option
    global sel_anal
    sel_anal = Label(analysis, text="",fg="green")
    sel_anal.configure(font='{} 8 {bold}')
    # sel_anal.place(anchor='w', relx='0.02', rely='0.8', x='0', y='0')
    sel_anal.grid(column=1,row=1,pady=10)



if __name__ == '__main__':

    ### Main Page ###

    ## Heading
    welcome = Label(root, text = "Welcome to PDP Sales Analysis!", fg = 'blue')
    # welcome.place(anchor='center', relx='0.5', rely='0.1', x='0', y='0')
    welcome.pack(pady=20)
    welcome.configure(font='{} 21 {bold underline}')



    filepath = LabelFrame(root, width=math.floor(3*w/4), height=h/4, text = "Database Filepath")
    filepath.pack(pady=h/10,fill='x',padx = 20)

    # File Location Label
    dbsel = Label(filepath, text= "Enter Database FilePath: ")
    dbsel.configure(font='{} 12 {italic}', text='Enter Database File Path: ')
    # dbsel.place(anchor='w', relx='0.05', rely='0.3', x='0', y='0')
    dbsel.pack(padx = 10,side  =LEFT,pady=h/20)

    # File Location Entry Box
    fileloctext = Entry(filepath,width=int(w/35))
    # fileloctext.place(anchor='w', relx='0.38', rely='0.3', width='350', height = '35', x='0', y='0')
    fileloctext.pack(side=LEFT, padx = 10)

    

    # Browse Button
    global browsebtn
    browsebtn = Button(filepath,height=1,width=4, text="Browse", command = dbselect)
    # browsebtn.place(anchor='w', height='35', relx='0.825', rely='0.3', width='100', x='0', y='0')
    browsebtn.pack(side=LEFT, padx = 5)

    # # File Format Label
    # errortext = "Please select file with .xlsx format"
    # errorlabel = Label(filepath, text = errortext,fg = 'red')
    # # errorlabel.place(anchor='w', relx='0.4', rely='0.36', x='0', y='0')
    # errorlabel.pack(side=BOTTOM)

    # Enter Button
    enter = Button(filepath, text="Enter",height=2,width=4,command= lambda: check_file(fileloctext.get()))
    # enter.place(anchor='nw', height='75', relx='0.73', rely='0.4', width='200', x='0', y='0')
    enter.pack(side=RIGHT,padx=10,pady=10)

    
    
    root.mainloop()