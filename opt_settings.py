from tkinter import *
from common_fns import *

w = 800
h = 600
windgeom = str(w) +"x"+ str(h)

def more_opt():
    destroyer([more_btn])

    c = entity + " to be compared with"
    name_input(c)

    ## Specific Selection Options
    notk = entlist.index(entity)
    print(entity,notk)
    n = names[0]

    global select_lf
    select_lf = []

    nindex = entity_list.index(names[0])
    mainchecklist = []
    totallist = []
    for i in range(len(index)):
        if i!=notk:
            print(i)
            lf_text = "Specific "+ entlist[i] + " Options"
            select_lf.append( LabelFrame( top, text=lf_text, height=200,width=200))
            select_lf[len(select_lf)-1].pack(side=LEFT,padx = 75,pady=1)
            sellist = []
            checklist = []
            for j in range (int(pdp[nindex][0][2])):
                a = pdp[nindex][j+2][index[i]]
                a=a.upper()
                rno = 0
                cno = -1
                if a not in sellist:
                    sellist.append(a)
                    var = IntVar()
                    check = Checkbutton(select_lf[len(select_lf)-1],text=a,variable=var)
                    
                    checklist.append(var)
        
                    if cno>=4:
                        cno=0
                        rno+=1
                    else:
                        cno+=1
                    # check.grid(row=rno,column=cno)
                    check.pack()
            totallist.append(sellist)
            mainchecklist.append(checklist)

    print(len(totallist))
            

        # for i in range(int(pdp[cindex][0][2])):
        #     p = pdp[cindex][i+2][8]
        #     p = p.upper()
        #     pdp[cindex][i+2][8] = p
        #     if p not in plist:
        #         plist.append(p)
        #     print(plist)

        #     for i in range(int(pdp[cindex][0][2])):
        #     e = pdp[cindex][i+2][7]
        #     e = e.upper()
        #     pdp[cindex][i+2][7] = e
        #     if e not in elist:
        #         elist.append(e)
        #     print(elist)
    

def get_name():

    names.append("")
    nlen = len(names)
    for i in poss_list.curselection():
        names[len(names)-1] = poss_list.get(i)
    
    if names[nlen-1] !="":
        nindex = entity_list.index(names[nlen-1])

        ent_btn.configure(state= DISABLED)
        send_btn.configure(state = DISABLED)

        if nlen==1:
            global more_btn
            more_btn = Button(n_input, text="More Options",command= lambda:more_opt() )
            more_btn.grid(column=3,row=1,padx=10)

        name_disp = Label(n_input, text=names[nlen-1])
        name_disp.configure(font = '{} 12 {italic}',fg='blue')
        name_disp.grid(column=3,row=0,padx=10)

        destroyer([send_btn , poss_list])

        final_btn = Button(top, text='RESULTS', bg="green", fg = "white")
        final_btn.place(anchor='w', height='70', x='675', y='550', width='100')

    
    else:
        errormsg = messagebox.showwarning("No ",entity," Selected!","Please Select a ",entity," Name from the ListBox!")

    print(" Selected Company is ",names[nlen-1])


def check_n():
    n= n_entry.get()
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

        try:
            if names[0] in poss_name:
                poss_name.remove(poss_name[poss_name.index(names[0])])
        except:
            poss_name.sort()
        poss_name.sort()
        print(poss_name)

        global poss_list
        poss_list = list_maker(n_input, poss_name, 5 )
        poss_list.grid(row=1,column=1,pady=5)

        global send_btn
        send_btn = Button(n_input, text="Enter",command=lambda: get_name())
        send_btn.grid(column=2,row=1,padx=10)

        print(poss_list.curselection)

    case_label = Label(n_input, text=check_flag)
    case_label.configure(font='{} 12 {bold}', fg = check_color, bg = "white")
    case_label.place(anchor='w',height='20',width='20',x='410',y='23')


def name_input(c):
    global n_input
    n_input = LabelFrame(top, text=c, height = 100)
    n_input.pack(fill='x', padx=20,pady=10)

    header = Label(n_input, text= "Enter "+entity+" Name:")
    header.configure(font='{} 10 {italic}')
    header.grid(row=0,column=0,padx=5,pady=10)

    global n_entry
    n_entry = Entry( n_input, width=20)
    # n_entry.bind("<Return>",check_n())
    n_entry.grid(row=0,column=1,padx=5)
    

    global ent_btn
    ent_btn = Button(n_input, text="Search", command=lambda: check_n())
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
    global names
    names = []

    for i in range(int(pdp[0][0][0])):
        entity_list.append(pdp[i][0][1])
        count_list.append(int(pdp[i][0][2]))
    
    for i in pdp[0][1]:
        keys.append(i)
    #####

    global entlist
    entlist = alist
    global index
    index = aindex    
    # lol = Button(top, text="lol", height=5, width=5,command=name_input)
    # lol.pack()
    c = entity + " Name"
    name_input(c)



