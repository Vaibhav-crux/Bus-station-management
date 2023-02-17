from tkinter import *
from tkinter import messagebox
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

#Bus image 
busImage=PhotoImage(file='.\\Bus_for_project.png')
homeImage=PhotoImage(file='home.png')
Label(root,image=busImage).grid(row=0,column=0,padx=w//2.5,columnspan=13)

#online bus booking system
Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font='Arial 25 bold').grid(row=1,column=0,columnspan=13)
Label(root,text='Add Bus Route Details',fg='green',font='Arial 20 bold').grid(row=2,column=0,pady=h/40,columnspan=13)

def check():
    if len(busid.get())==0 or len(runningDate.get())==0 or len(seatAvail.get())==0:
        messagebox.showerror("value Error","Enter Details Properly")
    else:
        showdetails()

def showdetails():
    Label(root,text='Bus Details',fg='Red',bg='LightBlue1',font='Arial 15').grid(row=5,column=0, columnspan=13,pady=h//30)
    Label(root,text='Bus ID: ',font='Arial 13').grid(row=6,column=3)
    Label(root,text=busid.get(),font='Arial 13').grid(row=6,column=4)
    Label(root,text='Running Date: ',font='Arial 13').grid(row=6,column=5)
    Label(root,text=runningdate.get(),font='Arial 13').grid(row=6,column=6)
    Label(root,text='Seat Availability: ',font='Arial 13').grid(row=6,column=7)
    Label(root,text=seatAvail.get(),font='Arial 13').grid(row=6,column=8)


#Bus ID
Label(root,text='Bus ID',font='Arial 13').grid(row=3,column=2,pady=h/20)
busid=Entry(root)
busid.grid(row=3,column=3)

#Running Date
Label(root,text='Running Date',font='Arial 13').grid(row=3,column=4)
runningDate=Entry(root)
runningDate.grid(row=3,column=5)

#Seat Available
Label(root,text='Seat Available',font='Arial 13').grid(row=3,column=6)
seatAvail=Entry(root)
seatAvail.grid(row=3,column=7)

# Buttons for add edit and home
Button(root,text='Add Run',font='Arial 15',bg='pale green',command=check).grid(row=3,column=9)
Button(root,text='Delete Run',font='Arial 15',bg='pale green',fg="Black",command=check).grid(row=3,column=10)
Button(root,image=homeImage,font='Arial 15',bg='pale green').grid(row=4,column=8,pady=h/20)
root.mainloop()