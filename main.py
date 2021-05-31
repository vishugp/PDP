from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Database Selector')

def dbselect():
    root.filename = filedialog.askopenfilename(initialdir="/home/vishu/Downloads",
                                            title = "Select the database",
                                            )

    my_label = Label(root, text = root.filename).pack()

def open():
    root.destroy()
    top = Toplevel()
    top.title("Analysis Type")
    label = Label(top, text="Choose the Type of Analysis to be performed").grid(row = 1,column=2)
    analysis = ['Company based','Product type based','Timely Analysis','Employee based']
    typebtn = []
    for i in range(len(analysis)):
        typebtn.append(Button(top, text=analysis[i], command = top.destroy).grid(row=2,column=i+1))


btn1 = Button(root, text="Choose the Database File", command = dbselect).pack()
btn2 = Button(root, text="Enter",command = open).pack()

root.mainloop()