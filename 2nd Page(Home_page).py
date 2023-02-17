from tkinter import *
root=Tk()


def seat_booking():
    root.destroy()
    import Third_page as third
    third.main_3()

def add_new_bus_detail():
    root.destroy()
    import sixth_Page_Add_new_bus_details_page as sixth
    sixth.new_bus()

def check_booking_detail():
    root.destroy()
    import fifth_Page_Checking_booking as fifth
    fifth.entrycheck()


w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,columnspan=3,padx=w//2.5)
Label(root,text="Online Bus Booking System",fg="Red",bg="LightBlue",font="Arial 20 bold").grid(row=1,column=0,columnspan=3)
b1=Button(root,text="Seat Booking", font='Arial 15 bold',bg='pale green',command=seat_booking).grid(row=2,column=0)
b2=Button(root,text="Check Booked Seat", font='Arial 15 bold',bg='lime green',command=check_booking_detail).grid(row=2,column=1)
b3=Button(root,text="Add Bus Details", font='Arial 15 bold',bg='dark green',command=add_new_bus_detail).grid(row=2,column=2,pady=h//15)
Label(root,text="For Admin Only",font='Arial 10 bold',fg="Red").grid(row=5,column=0)
root.mainloop()
