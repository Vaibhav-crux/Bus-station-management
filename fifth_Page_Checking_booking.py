from tkinter import *
from tkinter import messagebox
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
busImage=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=busImage).grid(row=0,column=0,padx=w//2.5,columnspan=12)
Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font='Arial 20 bold').grid(row=1,column=0,columnspan=12,pady=h/50)
Label(root,text='Check Bus Booking',fg='dark green',font='Arial 15 bold',bg='pale green').grid(row=2,column=0,columnspan=12)
Label(root,text='Enter Your Mobile No:',font='Arial 10 bold').grid(row=3,column=4,pady=h/50)
mobNumber=Entry(root)
mobNumber.grid(row=3,column=5)
def checknumber(s):
    count=0
    for i in s:
        if i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9':
            count+=1
    if count==10:
        return True
    else:
        return False
def entrycheck():
    if len(mobNumber.get())!=10:
        messagebox.showerror('Value missing','Enter correct Mobile Number')
    elif checknumber(mobNumber.get())==False:
        messagebox.showerror('Invalid input','Enter number properly')
Button(root,text='Check Booking',command=entrycheck).grid(row=3,column=6)
root.mainloop()
