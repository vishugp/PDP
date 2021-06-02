## Company based Analysis

import pandas as pd
from tkinter import *
import numpy as np

def str_clean(name):
  rwords = ['LTD.','PVT.','PVT','LTD','LIMITED']
  s = str(name).upper()

  for i in rwords:
    if i in s:
      # print(s)
      s = s.replace(i,'')
  if 'SYSTEM' in s:
    s = s.replace('SYSTEM','SYSTEMS')
  if 'SYSTEMSS' in s:
    s = s.replace('SYSTEMSS','SYSTEMS')
    # print(s)
  s = s.strip()
  return s

def name_analysis(i,zn):
  print("\nCompany No.",zn,"in the list is:")
  print("Name of the company: ",companies[i])
  print("No. of sale(s) : ",counts[i])
  print("Total Sales = ",pdp[i][counts[i]+1][3])

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
  
  for j in range(counts[i]):
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

def submit(compname):
    n = compname.get()
    n = n.upper()
    z=0
    for j in companies:
        if (n in j) and (j.index(n)==0 or j[j.index(n)-1]==" "):
            z+=1
            i = companies.index(j)
            name_analysis(i,z)
    if (z==0):
        print("Company with the word '",n,"' is not in the list!")

def create_df(fileloc):
    dataset = pd.ExcelFile(fileloc)
    df = dataset.parse(dataset.sheet_names[0])

    global companies
    global counts
    global keys

    companies = list()
    counts = list()
    indices = [8,3,5,6,9,1,7]
    keys = list()
    for i in indices:
        keys.append(df.columns[i])
    print(keys)

    global pdp

    pdp = np.empty([1000,100,len(keys)], dtype = "<U20")
    print(pdp.shape)

    for j in range(len(dataset.sheet_names)-1):
        df = dataset.parse(dataset.sheet_names[j])
        for i in range(df.shape[0]):
            # Column 2 is the Column of Organizations
            comp_name = str_clean(df[df.columns[2]][i])

            if comp_name == "NAN":
                continue
            if(comp_name not in companies):
                companies.append(comp_name)
                counts.append(1)
        
            else:
                counts[companies.index(comp_name)]+=1
                if(counts[companies.index(comp_name)] > 100):
                    print(">100 : ",comp_name, counts[companies.index(comp_name)])
                    print(j)


            index = companies.index(comp_name)
            # print(index,comp_name)
            for k in range(len(keys)):
                # print(df[keys[k]][i])
                pdp[index][counts[index]-1][k] = df[keys[k]][i]
                # print(pdp[index][counts[index]+1][k])
    
    print("No. of Companies: ",len(companies))
    print(counts)
    companies.sort()
    # print(companies)
    for i in companies:
      print(i)

def company_based(layer,loc):
    print("Company Based Analysis")
    fileloc = loc.filename
    create_df(fileloc)

    compname = StringVar()

    name_label = Label(layer, text="Enter the Company Name")
    comp_name = Entry(layer, 
                    textvariable= compname,
                    font=('calibre',10, 'bold')
                        )
    entry_btn =  Button(layer, text = "Enter", command =lambda: submit(compname))

    name_label.grid(row=0,column=0)
    comp_name.grid(row=0,column=2)
    entry_btn.grid(row=0,column=4)

    layer.mainloop()
    


