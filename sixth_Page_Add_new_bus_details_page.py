from tkinter import *
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

def new_operator():
    root.destroy()
    import Seventh_Page_New_Operator as seven
    seven.checking()

def add_bus():
    root.destroy()
    import eighth_Page_New_Bus as eight
    eight.checking()

def new_rout():
    root.destroy()
    import ninth_Page_New_Route as nine
    nine.check()

def new_run():
    root.destroy()
    import tenth_Page_New_Run as ten
    ten.showdetails
def new_bus():
#Adding bus image 
    busImage=PhotoImage(file='.\\Bus_for_project.png')
    Label(root,image=busImage).grid(row=0,column=0,padx=w//2.5,columnspan=12)

#Adding text
    Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font='Arial 20 bold').grid(row=1,column=0,columnspan=12)

#Page Detail
    Label(root,text='Add New Details to Database',fg='green',font='Arial 15 bold').grid(row=2,column=0,pady=h/40,columnspan=12)

#Buttons
    Button(root,text='New Operator',bg='pale green',font='Arial 15',command=new_operator).grid(row=3,column=4)
    Button(root,text='New Bus',font='Arial 15',bg='salmon1',command=add_bus).grid(row=3,column=5)
    Button(root,text='New Route',font='Arial 15',bg='cornflower Blue',command=new_rout).grid(row=3,column=6)
    Button(root,text='New Run',font='Arial 15',bg='indian red',command=new_run).grid(row=3,column=7)

    root.mainloop()
new_bus()