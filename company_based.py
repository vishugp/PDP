## Company based Analysis

from common_fns import *
import pandas as pd
from tkinter import messagebox
from tkinter import *
import numpy as np

def name_analysis(i,zn):
  print("\nCompany No.",zn,"in the list is:")
  print("Name of the company: ",company_list[i])
  print("No. of sale(s) : ",sales_list[i])
  print("Total Sales = ",pdp[i][sales_list[i]+3][3])

  indices = ''
  for j in range(len(keys)):
    indices+=keys[j]

    z = 25*(j+1) - len(indices)
    # print(z)
    for l in range (z):
      indices+= ' '
  
  indices = "  Sno  " + indices
  dash = ""
  for m in range(len(indices)):
    dash+="_"
  print(dash)
  print(indices)
  print(dash)
  
  for j in range(sales_list[i]):
    row = ''
    for k in range(pdp.shape[2]):
      row+=pdp[i][j][k]
      z = 25*(k+1) - len(row)
      # print(z)

      for l in range (z):
        row+= ' '
    
    spaces = ""
    for v in range(5 - len(str(j+1))):
      spaces +=" "
    row = "  " + str(j+1) + spaces + row
    print(row)

  print(dash)

def result(top,cname,plist,elist):
  print("LOL")
def more_opts(root,top,cname):

  cindex = company_list.index(cname)


  plabel = Label(top, text="Select Product Type(s):")
  plabel.place(anchor='w', relx='0.15', rely='0.4', x='0', y='0')
  plist = list()
  for i in range(int(pdp[cindex][0][2])):
    p = pdp[cindex][i+2][8]
    p = p.upper()
    pdp[cindex][i+2][8] = p
    if p not in plist:
      plist.append(p)
  # print(plist)
  plistbox = list_maker(top,plist,len(plist) )
  plistbox['selectmode'] = "multiple"
  plistbox.place(anchor='w', relx='0.15', rely='0.5', x='0', y='0')


  elabel = Label(top, text="Select Employee(s):")
  elabel.place(anchor='w', relx='0.65', rely='0.4', x='0', y='0')
  elist = list()
  for i in range(int(pdp[cindex][0][2])):
    e = pdp[cindex][i+2][7]
    e = e.upper()
    pdp[cindex][i+2][7] = e
    if e not in elist:
      elist.append(e)
  print(elist)
  elistbox = list_maker(top,elist ,len(elist))
  elistbox['selectmode'] = "multiple"
  elistbox.place(anchor='w', relx='0.65', rely='0.5', x='0', y='0')



def get_cname(root,top):
  cname = ""
  for i in clist.curselection():
    z=i
    cname = clist.get(i)

  if cname!="":
    cbtn.configure(state = DISABLED)
    searchbtn.configure(state=DISABLED)

    moptbtn = Button(top, text="More Options", command=lambda: more_opts(root,top,cname))
    moptbtn.place(anchor="w", relx ='0.8',rely = '0.3' )
    

    cnamedisp = Label(top, text =cname)
    cnamedisp.configure(font='{} 9 {italic}',fg ="blue")
    cnamedisp.place(anchor="w", relx ='0.8',rely = '0.25' )
    
    resultbtn = Button(top, text="Results")
    resultbtn.place(anchor='w', height='70', relx='0.8', rely='0.9', width='100', x='0', y='0')


  else:
    errormsg = messagebox.showwarning("No Company Selected!","Please Select a Company Name from the ListBox!")
    

  

  print(cname)
  


def check_company(n,top,root):
  flag1 = 0
  n = n.upper()
  z=0
  checkcase = ""
  possible_names = list()
  for j in company_list:
    if (n in j) and (j.index(n)==0 or j[j.index(n)-1]==" "):
      z+=1
      possible_names.append(j)
      i = company_list.index(j)
      # name_analysis(i,z)
  if (z==0):
    flag1=0
    checkcase = "✗"
    casecolor = "red"
    print("Company with the word '",n,"' is not in the list!")
    
  else:
    flag1 = 1
    checkcase = "✓"
    casecolor = "green"
    possible_names.sort()
    
    global clist
    clist = list_maker(top,possible_names,5)
    clist.place(anchor='w', relx='0.56', rely='0.25', x='0', y='0')

    global cbtn
    cbtn = Button(top, text="Enter",command=lambda: get_cname(root,top))
    cbtn.place(anchor="w", relx ='0.8',rely = '0.2' )

    print(clist.curselection)
    
   
  exlabel = Label(top, text=checkcase)
  exlabel.configure(font='{} 12 {bold}', fg=casecolor, bg = "white")
  exlabel.place(anchor='w', height='30', relx='0.51', rely='0.2', width='30', x='0', y='0')

  
def company_window(top,root):
  global pdp
  pdp = database_maker(root.filename,2)
   
  global company_list
  global sales_list
  global keys
  company_list=list()
  sales_list = list()
  keys = list() 

  for i in range(int(pdp[0][0][0])):
    company_list.append(pdp[i][0][1])
    sales_list.append(int(pdp[i][0][2]))


  for j in pdp[0][1]:
    # print(j)
    keys.append(j)


  root.withdraw()
  top.resizable(0,0)
  top.title("Company Based Analysis")
  # label = Label(top, text="CBA").pack()
  

  backbtn = Button(top, text="<==", command=lambda: back_fn(top,root))
  backbtn.place(anchor='nw', width='50', x='0', y='0')

  top.protocol("WM_DELETE_WINDOW",root.destroy)
  # label2 = Label(top, text=root.filename).pack()

  # Company Name Label
  cnamelabel = Label(top, text= "Enter Company Name: ")
  cnamelabel.configure(font='{} 12 {italic}')
  cnamelabel.place(anchor='w', relx='0.01', rely='0.2', x='0', y='0')

  # Company Name Entry Box
  cname = Entry(top)
  cname.place(anchor='w', relx='0.3', rely='0.2', width='200', height = '35', x='0', y='0')

  # Search Button
  global searchbtn
  searchbtn = Button(top, text="Search", command =lambda: check_company(cname.get(),top,root))
  searchbtn.place(anchor='w', height='30', relx='0.3', rely='0.27', width='200', x='0', y='0')

