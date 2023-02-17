from tkinter import *
from tkinter import messagebox
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

#Bus image
busImage=PhotoImage(file='.\\Bus_for_project.png')
homeImage=PhotoImage(file='home.png')
Label(root,image=busImage).grid(row=0,column=0,padx=w//2.5,columnspan=15)

#online bus booking system
Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font='Arial 25 bold').grid(row=1,column=0,columnspan=15)
Label(root,text='Add Bus Operation Details',fg='green',font='Arial 20 bold').grid(row=2,column=0,pady=h/40,columnspan=15)


def checkname(name):
    return name.isalpha()

def checkphone(phone):
    count=0
    for i in phone:
        if i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9':
            count+=1
    if count==10:
        return True
    else:
        return False

def checkemail(email):
    counta=0
    countb=0
    for i in email:
        if i=='@':
            count+=1
        if i=='.':
            countb+=1
    if counta==1 and countb>0:
        return True
    else:
        return False

def checking():
    if len(op_id.get())==0 or len(name.get())==0 or len(address.get())==0 or len(phone.get())!=10 or len(email_id.get())==0:
        messagebox.showerror('Value Error','Enter details properly')
    else:
        if checkname(name.get())==False:
            messagebox.showerror('Value Error','Enter details properly')
        if checkphone(phone.get())==False:
            messagebox.showerror('Value Error','Enter details properly')
        if checkemail(email_id.get())==False:
            messagebox.showerror('Value Error','Enter details properly')

#Operator ID
Label(root,text='Operator id',font='Arial 13').grid(row=3,column=2)
op_id=Entry(root)
op_id.grid(row=3,column=3)

#Name
Label(root,text='Name',font='Arial 13').grid(row=3,column=4)
name=Entry(root)
name.grid(row=3,column=5)

#Address
Label(root,text='Address',font='Arial 13').grid(row=3,column=6)
address=Entry(root)
address.grid(row=3,column=7)

#Phone
Label(root,text='Phone',font='Arial 13').grid(row=3,column=8)
phone=Entry(root)
phone.grid(row=3,column=9)

#Email ID
Label(root,text='Email id',font='Arial 13').grid(row=3,column=10)
email_id=Entry(root)
email_id.grid(row=3,column=11)

# Buttons for add edit and home
Button(root,text='Add',font='Arial 15',bg='pale green',command=checking).grid(row=3,column=12)
Button(root,text='Edit',font='Arial 15',bg='pale green').grid(row=3,column=13)
Button(root,image=homeImage,font='Arial 15',bg='pale green').grid(row=4,column=2,columnspan=15,pady=h/50)
mainloop()

