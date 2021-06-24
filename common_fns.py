from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd

def back_fn(top,root):
    top.withdraw()
    root.deiconify()
    
    # btn_fnl.config(state = wutstate)

def new_window(title,geom):
    window = Toplevel()
    # print(title)
    window.title(title)
    window.geometry(geom)
    return window

def str_opt(name):
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

def database_maker(fileloc,key):
    dataset = pd.ExcelFile(fileloc)
    df = dataset.parse(dataset.sheet_names[0])

    m_entity = list()
    counts = list()
    # total = list()
    # indices = [8,3,5,6,9,1,7]

    cols = list()
    for i in df.columns:
        cols.append(i)
    print(cols)

    pdp = np.empty([1000,1000,len(cols)], dtype = "<U20")
    # print(pdp.shape)

    for j in range(len(dataset.sheet_names)-1):
        df = dataset.parse(dataset.sheet_names[j])
        for i in range(df.shape[0]):

            ##### Company is in COLUMN 2
            entity = str_opt(df[df.columns[key]][i])

            if entity == "NAN":
                continue

            if entity not in m_entity:
                m_entity.append(entity)
                counts.append(1)
                # total.append(df[cols[i]][6])
                pdp[m_entity.index(entity)][0][1] = entity #Keeping Name in [0,1]
                # pdp[m_entity.index(entity)][0][3] = int(df[cols[i]][6])
                for k in range(len(cols)):
                    pdp[m_entity.index(entity)][1][k] = cols[k] #Setting the colunmn index
            else:
                counts[m_entity.index(entity)]+=1
                # total[m_entity.index(entity)]+=int(df[cols[i]][6])
                # pdp[m_entity.index(entity)][0][3] += int(df[cols[i]][6])


            cindex = m_entity.index(entity)
            
            for k in range(len(cols)):
                pdp[cindex][counts[cindex] + 1][k] = df[cols[k]][i]

    for i in range(len(m_entity)):
        # pdp[i][0][0] = m_entity[i]
        pdp[i][0][2] = int(counts[i])
        # print(pdp[i][0][1],"=",pdp[i][0][2])
    pdp[0][0][0] = int(len(m_entity))
    # for i in range(int(pdp[0][0][2]) +2):
    #     print(pdp[0][i])
    # print(m_entity)
    return pdp
    


def list_maker(window, list_opts, listsize):
    # if len(list_opts)<5:
    #     listsize = len(list_opts)
    # else:
    #     listsize = 5
    list = Listbox(window, width=25,height = listsize, font = '{} 8 {bold}', selectmode=BROWSE)
    for i in range(len(list_opts)):
        list.insert(i,list_opts[i])
    return list

def disabler(feature):
    feature['state']=DISABLED

def check_sel(listbox,btn):
    a= list()
    for i in listbox.curselection():
        a.append(listbox.get(i))
    if len(a)==0:
        errormsg = messagebox.showwarning("Select an option!","Please Select an option from the list before hitting the Enter Button!!!!!")
    else:
        disabler(listbox)
        disabler(btn)

def destroyer(widget_list):
    for widget in widget_list:
        widget.destroy()

def fdestroyer(root,k):
    # print(k)
    # if( (len(root.winfo_children())-1) >= k):
    #     print("Deleting children below",k)
    #     while(len(root.winfo_children())>k):
    #         root.winfo_children()[k].destroy()
    print(root.winfo_children())
    cno = len(root.winfo_children())
    print(cno)
    if cno-1 > k:
        while len(root.winfo_children())-1!=k:
            root.winfo_children()[k+1].destroy()
