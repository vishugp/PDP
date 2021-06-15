## Company based Analysis

from common_fns import *
import pandas as pd
from tkinter import messagebox
from tkinter import *
import numpy as np
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import math


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

def result_display(cname, top1, root,frame, k):
  print("LOL")
  # top1.withdraw()
  # root.deiconify()
  # res = new_window("RESULTS","1920x1080")
  # res.configure(bg='white')
  # res.wm_protocol("WM_DELETE_WINDOW",lambda: [res.destroy(),top1.deiconify()])  

  info = LabelFrame(frame,text="SELECTED OPTIONS")
  info.pack(fill='x',padx=5)
  # frame.grid(row=k,column=k,padx=10,pady=5)
  # framebg = frame['bg']

  # cnametext = "Company Name: " + cname
  # cnamelabel = Label(frame, text= cnametext, bg=framebg)
  # cnamelabel.configure(font='{} 10 {bold}')
  # cnamelabel.place(anchor='w', x='10', y='10')
  # cnamelabel.grid(row =0,column=0, padx=20, pady=5)
  # cnamelabel.pack()

  plistsel = list()
  elistsel = list()
  ptext = "Product type(s) Selected: "
  etext = "Employees dealing  with this customer: "

  try:
    if pbtn['state']==DISABLED:
      for i in plistbox.curselection():
        p = plistbox.get(i)
        plistsel.append(p)
      pplist = plistsel
    else:
      pplist = plist
  except:
    pplist = plist
  for i in range(len(pplist)-1):
    ptext = ptext + pplist[i] + ", "
  print(pplist)
  ptext += pplist[-1]

  pnamelabel = Label(info, text= ptext)
  pnamelabel.configure(font='{} 10 {bold}')
  # pnamelabel.place(anchor='w',  x='10', y='30')
  pnamelabel.pack(padx=10,pady=10)


  try:
    if ebtn['state']==DISABLED:
      for i in elistbox.curselection():
        e = elistbox.get(i)
        elistsel.append(e)
      eelist = elistsel
    else:
      eelist = elist
  except:
    eelist = elist
  for i in range(len(eelist)-1):
    etext = etext + eelist[i] + ", "
  etext += eelist[-1]

  enamelabel = Label(info, text= etext)
  enamelabel.configure(font='{} 10 {bold}')
  # enamelabel.place(anchor='w' ,x='10', y='50')
  enamelabel.pack(padx=10)

  sales = LabelFrame(frame,text="SALES")
  sales.pack(fill='x',padx=5)
  tree = ttk.Treeview(sales,height=5)
  # scrllbr = ttk.Scrollbar(frame , command=tree.yview)
  # tree.place(anchor='nw',x='850',y='20',height='150',width='1001')
  tree.pack(pady=10)
  # scrllbr.place(anchor='nw',x='1851',y='20',width='20',height='150')
  # scrllbr.pack()
  # tree.configure(xscrollcommand=scrllbr.set)

  indices = [8,3,5,6,9,1,7]
  collist = list()
  for i in range(len(indices)):
    collist.append(i+1)
  tree["columns"] = collist
  tree["show"] = 'headings'

  cindex = company_list.index(cname)
  for i in range(len(indices)):
    tree.column(i+1, width = math.floor(framew/len(indices)), anchor='c')
    tree.heading(i+1,text= pdp[cindex][1][indices[i]])

  nsales = int(pdp[cindex][0][2])
  print(nsales)
  for i in range(nsales):
    row = list()
    for j in range(len(indices)):
      data = pdp[cindex][2+i][indices[j]]
      if indices[j] == 1:
        data = data[:10]
      row.append(data)
    tree.insert("",'end', values=row)



  pcount = [0]*len(plist)
  for i in range(nsales):
    for j in plist:
      if pdp[cindex][2+i][8]== j:
        pcount[plist.index(j)]+= int(pdp[cindex][2+i][5][:-2])
  for i in pcount:
    i= (i/sum(pcount))*100
  explode = [0]*len(plist)
  if pplist != plist:
    for i in pplist:
      if i in pplist:
        # print('sliced')
        explode[plist.index(i)]=0.5


  g1 = LabelFrame(frame,width = framew/6,height=framew/6,text="Graph 1")
  g1.pack(side=LEFT,padx=5)
  graph1label =Label(g1, text = "PRODUCT SALES PIE CHART")
  graph1label.configure(font='{} 10 {bold}')
  # # graph1label.place(anchor='nw',x='150',y='270')
  graph1label.pack()

  fig1, ax1 = plt.subplots()
  ax1.pie(pcount,explode=explode, labels=plist, autopct='%1.1f%%',startangle=90, pctdistance=1.1,labeldistance=1.3)
  plt.legend(plist, loc="best" )
  ax1.axis('equal')
  plt.plot()

  graph1 = FigureCanvasTkAgg(fig1,master = g1) 
  graph1.draw()
  # # placing the graph1 on the Tkinter window
  # # graph1.get_tk_widget().place(anchor='nw',x='100',y='300',width=750,height=750)
  graph1.get_tk_widget().pack()
  # # creating the Matplotlib toolbar
  toolbar = NavigationToolbar2Tk(graph1,g1)
  toolbar.update()
  
  #   # placing the toolbar on the Tkinter window
  # # graph1.get_tk_widget().place(anchor='nw',x='100',y='300',width=750,height=750)
  graph1.get_tk_widget().pack()

  


def result(top1,root,cname1,cname2):
  top1.withdraw()
  # root.deiconify()
  global w,h,framew,frameh
  cname2 = "SWASTIK"
  # cname2=""
  if cname2=="":
    w=1440
    h=810
    framew = w-30
    frameh =h
    filler = "both"
  else:
    w=1920
    # h=1080
    h=1010
    framew = w/2 - 30
    frameh = h
    filler  ="y"
  
  resgeom = str(w)+ "x" + str(h)
  res = new_window("RESULTS",resgeom)
  res.resizable(0,0)
  # res.configure(bg='white')
  res.wm_protocol("WM_DELETE_WINDOW",lambda: [res.destroy(),top1.deiconify()])  

  
  framebg = "grey"

  frame1= LabelFrame(res, width=framew ,height=frameh,relief="sunken",borderwidth=2,text=cname1)
  frame1.pack(side=LEFT,expand=FALSE,fill=filler,padx=10,pady=10)
  vscrlbr = Scrollbar(res, orient='vertical')
  vscrlbr.pack(side=LEFT,expand=FALSE,fill=Y)
  result_display(cname1,res,root,frame1,0)

  if cname2!="":
    frame2= LabelFrame(res, width=framew, height=frameh,relief="sunken",borderwidth=2,text=cname2)
    frame2.pack(side=RIGHT,fill=filler,expand="yes",padx=10,pady=10)
    result_display(cname2,res,root,frame2,0)
  
  

def more_opts(root,top1,cname):

  plabel = Label(top1, text="Select Product Type(s):")
  plabel.place(anchor='nw', x='25', y='275',height="25")
  global plistbox
  plistbox = list_maker(top1,plist,5 )
  plistbox['selectmode'] = "multiple"
  plistbox.place(anchor='nw', x='25', y='300')
  global pbtn
  pbtn = Button(top1, text="Enter ✓",fg="green",command=lambda:check_sel(plistbox,pbtn))
  pbtn.place(anchor='nw', height='25', width='75', x='125', y='400')


  elabel = Label(top1, text="Select Employee(s):")
  elabel.place(anchor='nw',x='250', y='275')
  global elistbox
  elistbox = list_maker(top1,elist ,5)
  elistbox['selectmode'] = "multiple"
  elistbox.place(anchor='nw', x='250', y='300')
  global ebtn
  ebtn = Button(top1, text="Enter ✓",fg="green",command=lambda: check_sel(elistbox,ebtn))
  ebtn.place(anchor='nw', height='25', width='75', x='350', y='400')


def get_cname(root,top1):
  cname1 = ""
  for i in clist.curselection():
    z=i
    cname1 = clist.get(i)

  if cname1!="":
    cindex = company_list.index(cname1)

    
    global plist
    plist = list()
    global elist
    elist = list()

    
    
    for i in range(int(pdp[cindex][0][2])):
      p = pdp[cindex][i+2][8]
      p = p.upper()
      pdp[cindex][i+2][8] = p
      if p not in plist:
        plist.append(p)
    print(plist)

    for i in range(int(pdp[cindex][0][2])):
      e = pdp[cindex][i+2][7]
      e = e.upper()
      pdp[cindex][i+2][7] = e
      if e not in elist:
        elist.append(e)
    print(elist)

    cbtn.configure(state = DISABLED)
    searchbtn.configure(state=DISABLED)

    moptbtn = Button(top1, text="More Options", command=lambda: more_opts(root,top1,cname1))
    moptbtn.place(anchor="w", x ='630',y = '210',height='50' )
    

    cnamedisp = Label(top1, text =cname1)
    cnamedisp.configure(font='{} 8 {italic}',fg ="purple")
    cnamedisp.place(anchor="w", x ='665',y = '150',height="50")
    
    cname2="Company 2"
    resultbtn = Button(top1, text="Results",bg = "green" , fg = "white",command=lambda:result(top1,root,cname1,cname2))
    resultbtn.place(anchor='w', height='70', x='675', y='550', width='100')


  else:
    errormsg = messagebox.showwarning("No Company Selected!","Please Select a Company Name from the ListBox!")

  print(cname1)
  


def check_company(n,top1,root):
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
    clist = list_maker(top1,possible_names,5)
    clist.place(anchor='nw', x='435', y='80',width='225')

    global cbtn
    cbtn = Button(top1, text="Enter",command=lambda: get_cname(root,top1))
    cbtn.place(anchor="w", x = '670',y='100', width = "100", height = "25" )

    print(clist.curselection)
    
   
  exlabel = Label(top1, text=checkcase)
  exlabel.configure(font='{} 12 {bold}', fg=casecolor, bg = "white")
  exlabel.place(anchor='w', height='30', width='30', x='385', y='100')

  
def company_window(top1,root):
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
  top1.resizable(0,0)
  top1.title("Company Based Analysis")
  # label = Label(top1, text="CBA").pack()
  

  backbtn = Button(top1, text="<==", command=lambda: back_fn(top1,root))
  backbtn.place(anchor='nw', width='50', x='0', y='0')

  top1.protocol("WM_DELETE_WINDOW",root.destroy)
  # label2 = Label(top1, text=root.filename).pack()

  # Company Name Label
  cnamelabel = Label(top1, text= "Enter Company Name: ")
  cnamelabel.configure(font='{} 10 {bold}')
  cnamelabel.place(anchor='w', x='5', y='100')

  # Company Name Entry Box
  cname = Entry(top1)
  cname.place(anchor='w', width='200', height = '40', x='225', y='100')

  # Search Button
  global searchbtn
  searchbtn = Button(top1, text="Search", command =lambda: check_company(cname.get(),top1,root))
  searchbtn.place(anchor='w', height='30', width='200', x='225', y='150')

