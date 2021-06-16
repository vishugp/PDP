# Employee Based Analysis
from common_fns import *

def get_ename(root,top1):
    ename1=""
    for i in elist.curselection():
        z=i
        ename1 = elist.get(i)

    if ename1!="":
        eindex = employee_list.index(ename1)

        ebtn.configure(state = DISABLED)
        searchbtn.configure(state=DISABLED)

        moptbtn = Button(name_input, text="More Options", command=lambda: more_opts(root,top1,ename1))
        # moptbtn.place(anchor="w", x ='630',y = '210',height='50' )
        moptbtn.grid(column=3,row=1,padx=10)
        

        enamedisp = Label(name_input, text =ename1)
        enamedisp.configure(font='{} 12 {italic}',fg ="green")
        # cnamedisp.place(anchor="w", x ='665',y = '150',height="50")
        enamedisp.grid(column=3,row=0,padx=10)
        
        ename2="Company 2"
        resultbtn = Button(top1, text="Results",bg = "green" , fg = "white",command=lambda:result(top1,root,ename1,ename2))
        resultbtn.place(anchor='w', height='70', x='675', y='550', width='100')


def check_employee(n,top1,root):
  flag1 = 0
  n = n.upper()
  z=0
  checkcase = ""
  possible_names = list()
  for j in employee_list:
    if (n in j) and (j.index(n)==0 or j[j.index(n)-1]==" "):
      z+=1
      possible_names.append(j)
      i = employee_list.index(j)
      # name_analysis(i,z)
  if (z==0):
    flag1=0
    checkcase = "✗"
    casecolor = "red"
    print("Employee with the word '",n,"' is not in the list!")
    
  else:
    flag1 = 1
    checkcase = "✓"
    casecolor = "green"
    possible_names.sort()
    
    global elist
    elist = list_maker(name_input,possible_names,5)
    # elist.place(anchor='nw', x='435', y='80',width='225')
    elist.configure(width=25)
    elist.grid(row=1,column=1,pady=5)

    global ebtn
    ebtn = Button(top1, text="Enter",command=lambda: get_ename(root,top1))
    # ebtn.place(anchor="w", x = '670',y='100', width = "100", height = "25" )
    ebtn.grid(column=2,row=1, padx=10)
    print(elist.curselection)
    
   
  exlabel = Label(top1, text=checkcase)
  exlabel.configure(font='{} 12 {bold}', fg=casecolor, bg = "white")
  exlabel.place(anchor='w', height='20', width='20', x='4250', y='105')


def emp_based(top1,root):
    global pdp
    pdp = database_maker(root.filename,7)

    global employee_list
    global count_list
    global keys

    employee_list = list()
    count_list = list()
    keys = list()

    for i in range(int(pdp[0][0][0])):
        employee_list.append(pdp[i][0][1])
        count_list.append(int(pdp[i][0][2]))


    for j in pdp[0][1]:
        # print(j)
        keys.append(j)

    top1.resizable(0,0)
    top1.title("Employee Based Analysis")

    backbtn = Button(top1, text="<==", command=lambda: back_fn(top1,root))
    backbtn.place(anchor='nw', width='50', x='0', y='0')
    top1.protocol("WM_DELETE_WINDOW",root.destroy)

    analtypelabel = Label(top1, text="EMPLOYEE BASED ANALYSIS",fg="red")
    analtypelabel.configure(font='{} 14 {bold underline}')
    analtypelabel.pack(pady=10)

    global name_input
    name_input = LabelFrame(top1, text="Employee Name",height=100)
    name_input.pack(fill='x',padx=20,pady=10)

    # Employee Name Label
    enamelabel = Label(name_input, text= "Enter Employee Name: ")
    enamelabel.configure(font='{} 10 {italic}')
    # enamelabel.place(anchor='w', x='5', y='100')
    enamelabel.grid(row=0,column=0,padx=5,pady=10)

    # Employee Name Entry Box
    ename = Entry(name_input,width=20)
    # ename.place(anchor='w', width='200', height = '40', x='225', y='100')
    ename.grid(row=0,column=1,padx=5)

    # Search Button
    global searchbtn
    searchbtn = Button(name_input, text="Search", command =lambda: check_employee(ename.get(),top1,root))
    # searchbtn.place(anchor='w', height='30', width='200', x='225', y='150')
    searchbtn.grid(row=0,column=2,padx=1)