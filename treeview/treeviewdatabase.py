from tkinter import*
from tkinter import ttk,messagebox
import treeviewdata

root=Tk()
root.title('treeview database')
root.config(bg="khaki4")
root.geometry("450x700")

#*****^^^^^*functions*******************
def exit():
	exit = messagebox.askyesno("client management system","ARE YOU SURE ?")
	if exit>0:
		root.destroy()
		return

def selectitem(event):
	global selecteditem
	clear()
	viewinfo=mytree.focus()
	leanerdata=mytree.item(viewinfo)
	selecteditem=leanerdata['values']
	enid.insert(END,selecteditem[1])
	enfirstname.insert(END,selecteditem[2])
	enlastname.insert(END,selecteditem[3])
	engender.insert(END,selecteditem[4])
	enemail.insert(END,selecteditem[5])
	enhours.insert(END,selecteditem[6])	
	enpayfor1.insert(END,selecteditem[7])
	entax.config(state='normal')
	entax.insert(END,selecteditem[8])
	entax.config(state='disabled')
	enpayment.config(state='normal')
	enpayment.insert(END,selecteditem[9])
	enpayment.config(state='disabled')
	
						
def cal():
	try:	
		if enhours.get()=="" or enpayfor1.get()=="" :
			messagebox.showerror("superviser","please include hours and payfor1 .")
			return
		else:
			totalpay=int(enhours.get())*int(enpayfor1.get())
			tax=totalpay*10/100
			entax.config(state="normal")
			entax.insert(END,tax)
			entax.config(state="disabled")
			entax.config(disabledforeground='black',disabledbackground="khaki1")
			payment = totalpay - tax
			enpayment.config(state="normal")
			enpayment.insert(END,payment)
			enpayment.config(state="disabled")
			enpayment.config(disabledforeground='black',disabledbackground="gold")
	except ValueError:
		messagebox.showerror("supervisor","you must include fields with number .")
		return
		
		
		
def clear():
	enid.delete(0,END)
	enfirstname.delete(0,END)
	enlastname.delete(0,END)
	engender.delete(0,END)
	enemail.delete(0,END)
	enhours.delete(0,END)
	enpayfor1.delete(0,END)
	entax.config(state='normal')
	entax.delete(0,END)
	entax.config(state='disabled')
	enpayment.config(state='normal')
	enpayment.delete(0,END)
	enpayment.config(state='disabled')
	
	
	
	
	
	
def clr():
	mytree.delete(*mytree.get_children())	
	
	
	
def add():
	if enid.get()=="" or enfirstname.get()=="" or enlastname.get()=="" or engender.get()=="" or enemail.get()=="" or enhours.get()=="" or enpayfor1.get()=="" :
		messagebox.showerror("supervisor","please include all fields .")
		return	
	else:
		clr()
		treeviewdata.adddata(enid.get(),enfirstname.get(),enlastname.get(),engender.get(),enemail.get(),enhours.get(),enpayfor1.get(),entax.get(),enpayment.get())
		mytree.insert(parent='',index=END,values=(enid.get(),enfirstname.get(),enlastname.get(),engender.get(),enemail.get(),enhours.get(),enpayfor1.get(),entax.get(),enpayment.get()))
		clear()
		viewdata()
		
		
def viewdata():
				result=treeviewdata.viewdata()
				if len(result) !=0:
					mytree.delete(*mytree.get_children())
					for row in result:
						mytree.insert(parent="",index=END,values=row)

			
def deldata():
		treeviewdata.deldata(selecteditem[0])
		clear()
		clr()
		viewdata()
	
		
									
#===========widget====================	
mainframe=Frame(root,bg="khaki4")
mainframe.pack()

titleframe=LabelFrame(mainframe,bg="khaki4",bd=5,relief=RIDGE)
titleframe.pack()
lbltitle=Label(titleframe,text="CLIENT MANAGEMENT SYSTEM",bg="khaki4",font="times 15 bold",padx=10)
lbltitle.pack()

style=ttk.Style()
style.theme_use('default')
style.configure("Treeview",background="khaki4",foreground="black",rowheight=24,fieldbackground="khaki4",font='times 10 bold')
style.map("Treeview",background=[("selected",'black')])


treeframe=LabelFrame(mainframe,bd=5,bg="khaki4",text="Treeview of client",relief=RIDGE)
treeframe.pack()

treescroll=Scrollbar(treeframe)
treescroll.pack(side=RIGHT,fill=Y)
treescroll1=Scrollbar(treeframe,orient=HORIZONTAL)
treescroll1.pack(side=BOTTOM,fill=X)

mytree=ttk.Treeview(treeframe,yscrollcommand=treescroll.set,xscrollcommand=treescroll1.set,selectmode='extended')

mytree['columns']=("num","id","firstname","lastname","gender","email","hours","payfor1","tax","payment")

mytree.column("#0",width=0,stretch=NO)
mytree.column("num",anchor=CENTER,minwidth=80)
mytree.column("id",anchor=CENTER,width=100,minwidth=80)
mytree.column("firstname",anchor=W,width=240,minwidth=250)
mytree.column("lastname",anchor=W,width=240,minwidth=250)
mytree.column("gender",anchor=CENTER,width=240,minwidth=100)
mytree.column("email",anchor=W,width=240,minwidth=300)
mytree.column("hours",anchor=CENTER,width=240,minwidth=200)
mytree.column("payfor1",anchor=CENTER,width=240,minwidth=200)
mytree.column("tax",anchor=CENTER,width=240,minwidth=200)
mytree.column("payment",anchor=W,width=240,minwidth=200)

mytree.heading("#0",text="",anchor='center')
mytree.heading("num",text="",anchor='center')
mytree.heading("id",text="id",anchor='center')
mytree.heading("firstname",text="firstname",anchor='center')
mytree.heading("lastname",text="lastname",anchor='center')
mytree.heading("gender",text="gender",anchor='center')
mytree.heading("email",text="email",anchor='center')
mytree.heading("hours",text="hours",anchor='center')
mytree.heading("payfor1",text="payfor1",anchor='center')
mytree.heading("tax",text="tax",anchor='center')
mytree.heading("payment",text="payment",anchor='center')

treescroll.config(command=mytree.yview)
treescroll1.config(command=mytree.xview)
mytree.pack(fill='both',expand=True)
mytree.bind('<ButtonRelease-1>',selectitem)

f1=LabelFrame(mainframe,text='information',bg='khaki4',bd=5,relief=RIDGE)
f1.pack()
lblid=Label(f1,text='ID',bg='khaki4',anchor=W,font="times 10 bold",justify=LEFT)
lblid.grid(row=0,column=0,sticky=W)
enid=Entry(f1,font="times 10 bold",width=34)
enid.grid(row=0,column=1)

lblfirstname=Label(f1,text='firstname',bg='khaki4',font="times 10 bold")
lblfirstname.grid(row=1,column=0,sticky=W)
enfirstname=Entry(f1,font="times 10 bold",width=34)
enfirstname.grid(row=1,column=1)

lbllastname=Label(f1,text='lastname',bg='khaki4',font="times 10 bold")
lbllastname.grid(row=2,column=0,sticky=W)
enlastname=Entry(f1,font="times 10 bold",width=34,)
enlastname.grid(row=2,column=1)

lblgender=Label(f1,text='gender',bg='khaki4',font="times 10 bold")
lblgender.grid(row=3,column=0,sticky=W)
engender=Entry(f1,font="times 10 bold",width=34)
engender.grid(row=3,column=1)

lblemail=Label(f1,text='email',bg='khaki4',anchor=W,font="times 10 bold")
lblemail.grid(row=4,column=0,sticky=W)
enemail=Entry(f1,font="times 10 bold",width=34)
enemail.grid(row=4,column=1)

lblhours=Label(f1,text='hours',bg='khaki4',anchor=W,font="times 10 bold")
lblhours.grid(row=5,column=0,sticky=W)
enhours=Entry(f1,font="times 10 bold",width=34)
enhours.grid(row=5,column=1)

lblpayfor1=Label(f1,text='payfor1',bg='khaki4',font="times 10 bold")
lblpayfor1.grid(row=6,column=0,sticky=W)
enpayfor1=Entry(f1,font="times 10 bold",width=34)
enpayfor1.grid(row=6,column=1)

lbltax=Label(f1,text='tax',bg='khaki4',anchor=W,font="times 10 bold")
lbltax.grid(row=7,column=0,sticky=W)
entax=Entry(f1,font="times 10 bold",width=34,state=DISABLED)
entax.grid(row=7,column=1)

lblpayment=Label(f1,text='payment',bg='khaki4',font="times 10 bold")
lblpayment.grid(row=8,column=0,sticky=W)
enpayment=Entry(f1,font="times 10 bold",width=34,state=DISABLED)
enpayment.grid(row=8,column=1)

f2=LabelFrame(mainframe,bd=5,bg="khaki4",relief=RIDGE)
f2.pack()
btncal=Button(f2,text="cal",bg="khaki4",command=cal,height=2)
btncal.grid(row=0,column=0)

btnadd=Button(f2,text="add",bg="khaki4",command=add,height=2)
btnadd.grid(row=0,column=1)

btnsearch=Button(f2,text="search",bg="khaki4",height=2,command=clear)
btnsearch.grid(row=0,column=2)

btnview=Button(f2,text="view",bg="khaki4",command=viewdata,height=2)
btnview.grid(row=0,column=3)

btnupdate=Button(f2,text="update",bg="khaki4",height=2)
btnupdate.grid(row=0,column=4)

btndelete=Button(f2,text="delete",bg="khaki4",height=2,command=deldata)
btndelete.grid(row=0,column=5)

btnexit=Button(f2,text="exit",bg="khaki4",command=exit,height=2)
btnexit.grid(row=0,column=6)








root.mainloop()