from typing import KeysView
from common_fns import *

w = 800
h = 600
windgeom = str(w) +"x"+ str(h)

def check_n(n):
    n=n.upper()
    flag = 0
    check_flag = ""
    poss_name = list()

    for i in entity_list:
        if (n in i) and ( i.index(n)==0 or i[i.index(n)-1]==" " ):
            flag+=1
            poss_name.append(i)

    if (flag==0):
        check_flag = "✗"
        check_color = "red"
        print(entity," with the word '",n,"' is not in the list!")

    else:
        check_flag = "✓"
        check_color = "green"
        poss_name.sort()
        print(poss_name)

        poss_list = list_maker(n_input, poss_name, 5 )
        poss_list.grid(row=1,column=1,pady=5)

        send_btn = Button(n_input, text="Enter")
        send_btn.grid(column=2,row=1,padx=10)

        print(poss_list.curselection)

    case_label = Label(n_input, text=check_flag)
    case_label.configure(font='{} 12 {bold}', fg = check_color, bg = "white")
    case_label.place(anchor='w',height='20',width='20',x='410',y='23')


def name_input():
    global n_input
    n_input = LabelFrame(top, text=entity+" Name", height = 100)
    n_input.pack(fill='x', padx=20,pady=10)

    header = Label(n_input, text= "Enter "+entity+" Name:")
    header.configure(font='{} 10 {italic}')
    header.grid(row=0,column=0,padx=5,pady=10)

    n_entry = Entry( n_input, width=20)
    n_entry.grid(row=0,column=1,padx=5)

    ent_btn = Button(n_input, text="Search", command=lambda: check_n(n_entry.get()))
    ent_btn.grid(row=0,column=2,padx=3)


def settings(root,alist,aindex,k):
    
    ## Basic Window Setup
    global entity
    entity = alist[k]
    wtitle = entity + " Based Analysis"
    global top
    top = new_window(wtitle,windgeom)
    top.resizable(0,0)

    backbtn = Button(top, text="<==",command= lambda: back_fn(top,root))
    backbtn.place(anchor='nw', width='50',x='0',y='0')

    heading = Label(top, text= wtitle.upper(), fg="red")
    heading.configure(font = '{} 14 {bold underline}')
    heading.pack( pady=10)

    top.protocol("WM_DELETE_WINDOW",root.destroy)
    ##

    ## Database Prep
    global pdp
    pdp = database_maker(root.filename,aindex[k])

    global entity_list
    entity_list = list()
    global count_list
    count_list = list()
    global keys
    keys = list()

    for i in range(int(pdp[0][0][0])):
        entity_list.append(pdp[i][0][1])
        count_list.append(int(pdp[i][0][2]))
    
    for i in pdp[0][1]:
        keys.append(i)
    #####
    
    lol = Button(top, text="lol", height=5, width=5,command=name_input)
    lol.pack()
    # name_input()



