from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
from company_based import *
from product_based import *
from time_based import *
from emp_based import *

basis = ['Company based','Product type based','Time Dependent','Employee based']
flag1 = 0
windgeom = "800x600"
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
    top2 = Toplevel()
    print(basis[k])
    top2.title(basis[k])
    top2.geometry("800x600")
    

    if k==0:
        company_based(top2,root)
    elif k==1:
        product_based(top2, root)
    elif k==2:
        time_based(top2,root)
    elif k==3:
        emp_based(top2,root)

def back(top):
    top.destroy()
    root.deiconify()
    browsebtn.config(state = NORMAL)

def open(z):
    root.withdraw()
    top = Toplevel()
    top.geometry(windgeom)
    top.resizable(0,0)
    top.title(basis[z]+" Analysis")
    label = Label(top, text=basis[z] + " Analysis")
    # root.deiconify()

    backbtn = Button(top, text="<==", command=lambda: back(top))
    backbtn.pack()
    top.protocol("WM_DELETE_WINDOW",root.destroy)
    # cbtn = Button(top, text=analysis[0], command=lambda:[top.destroy(), analysis_opt(0)])
    # pbtn = Button(top, text=analysis[1], command=lambda:[top.destroy(), analysis_opt(1)])
    # tbtn = Button(top, text=analysis[2], command=lambda:[top.destroy(), analysis_opt(2)])
    # ebtn = Button(top, text=analysis[3], command=lambda:[top.destroy(), analysis_opt(3)])

def anal():
    for i in analist.curselection():
        z = i
        opt = analist.get(i)
    flag1 = 0
    # Selected Option
    if browsebtn['state']== NORMAL:
        messagebox.showwarning("Database File Error", "Please Select the Database File!")

    else: 
        try:
            opt+=" ANALYSIS"
            opt=opt.upper()
            msgtext = "Database file: \n" + root.filename + "\nAnalysis type: \n" + opt
            final = messagebox.askyesno("Options?",msgtext)
            if final == True:
                open(z)
            else:
                browsebtn.configure(state=NORMAL)

            # sel_anal.configure(text=opt)
            flag1=1
        except:
            messagebox.showinfo("Select Analysis Type","Please Select the type of Analysis to be performed from the given List!")
            

    

def check_file(filenama):
    if root.filename=="":
        messagebox.showerror("File not Selected","Please Select Database File")
    # print(filenama)
    x = filenama.split(".")[-1]
    # print(type(filenama))
    # print(x)
    
    if x!="xlsx":
        messagebox.showerror("Invalid file Format","Please provide database file with '.xlsx' file format!")
    else:
        browsebtn.config(state = DISABLED)
    

if __name__ == '__main__':
    ## Heading
    welcome = Label(root, text = "Welcome to PDP Sales Analysis!")
    welcome.place(anchor='center', relx='0.5', rely='0.1', x='0', y='0')
    welcome.configure(font='{} 20 {bold underline}')

    # File Location Label
    dbsel = Label(root, text= "Enter Database FilePath: ")
    dbsel.configure(font='{} 12 {italic}', text='Enter Database File Path: ')
    dbsel.place(anchor='w', relx='0.05', rely='0.3', x='0', y='0')

    # File Location Entry Box
    fileloctext = Entry(root)
    fileloctext.place(anchor='w', relx='0.415', rely='0.3', width='400', x='0', y='0')


    # if ".xlsx" not in root.filename:
    #     errortext = "Please select file with .xlsx format"
    # else:
    #     errortext = ""
    # errorlabel = Label(root, text = errortext)
    # errorlabel.place(anchor='w', relx='0.47', rely='0.375', x='0', y='0')

    # Browse Button
    browsebtn = Button(root, text="Browse", command = dbselect)
    browsebtn.place(anchor='nw', height='50', relx='0.45', rely='0.45', width='150', x='0', y='0')

    # Enter Button
    enter = Button(root, text="Enter",command= lambda: check_file(root.filename))
    enter.place(anchor='nw', height='50', relx='0.73', rely='0.45', width='150', x='0', y='0')
    
    # Analysis Option
    opt_anal = Label(root, text= "Choose the type of analysis: ")
    opt_anal.configure(font='{} 12 {italic}')
    opt_anal.place(anchor='w', relx='0.05', rely='0.7', x='0', y='0')

    # Next Button
    next = Button(root, text="Next",command = anal)
    next.place(anchor='nw', height='75', relx='0.73', rely='0.67', width='200', x='0', y='0')
    
    # Analysis Types List
    analist = Listbox(root,height=4, selectmode=BROWSE)
    for i in range(len(basis)):
        analist.insert(i+1,basis[i])
    analist.place(anchor='n', relx='0.57', rely='0.67', x='0', y='0')

    # Selected option
    sel_anal = Label(root, text="")
    sel_anal.configure(font='{} 12 {bold}')
    sel_anal.place(anchor='w', relx='0.02', rely='0.8', x='0', y='0')


    root.mainloop()