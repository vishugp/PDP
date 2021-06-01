from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from company_based import *
from product_based import *
from time_based import *
from emp_based import *

analysis = ['Company based','Product type based','Timely Analysis','Employee based']


root = Tk()
root.title('Database Selector')
root.filename = ""
def dbselect():
    root.filename = filedialog.askopenfilename(initialdir="/home/vishu/Downloads",
                                            title = "Select the database",
                                            )
    my_label = Label(root, text = root.filename).grid(row=1,column=1)

def analysis_opt(k):
    top2 = Toplevel()
    print(analysis[k])
    top2.title(analysis[k])
    top2.geometry("900x600")
    

    if k==0:
        company_based(top2,root.filename)
    elif k==1:
        product_based(top2, root.filename)
    elif k==2:
        time_based(top2,root.filename)
    elif k==3:
        emp_based(top2,root.filename)



def open():
    root.withdraw()
    top = Toplevel()
    top.title("Analysis Type")
    label = Label(top, text="Choose the Type of Analysis to be performed").grid(row = 1,column=2)
    
    cbtn = Button(top, text=analysis[0], command=lambda:[top.destroy(), analysis_opt(0)]).grid(row=2,column=0)
    pbtn = Button(top, text=analysis[1], command=lambda:[top.destroy(), analysis_opt(1)]).grid(row=2,column=2)
    tbtn = Button(top, text=analysis[2], command=lambda:[top.destroy(), analysis_opt(2)]).grid(row=2,column=4)
    ebtn = Button(top, text=analysis[3], command=lambda:[top.destroy(), analysis_opt(3)]).grid(row=2,column=6)


btn1 = Button(root, text="Choose the Database File", command = dbselect).grid(row=0,column=1)
btn2 = Button(root, text="Enter",command = open).grid(row=2,column=1)
root.mainloop()