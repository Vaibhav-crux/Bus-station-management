from tkinter import *
from tkinter import messagebox
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

def main_3():

#gender drop_menu options
    gender_type=StringVar()
    gender_type.set("Gender")
    options_gender_type=["Male","Female","Others"]

#adding bus image to the page
    busImage=PhotoImage(file='.\\Bus_for_project.png')
    Label(root,image=busImage).grid(row=0,column=0,padx=w//2.5,columnspan=8)

#Adding Application name
    Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font='Arial 20 bold').grid(row=1,column=0,columnspan=8)
    Label(root,text='Enter Journey Details',bg='pale green',fg='dark green',font='Arial 15 bold').grid(row=2,column=0,columnspan=8,pady=h//20)

    root.mainloop()
#function to check if all fields are filled or not

def checkTo(boarding):
    return boarding.isalpha()

def checkFrom(destinate):
    return destinate.isalpha()

def checkDate(datee):
    s=[]
    s=datee.split('/')
    if len(s)==3:
        if s[0].isnumeric() and s[1].isnumeric() and s[2].isnumeric():
            if (int)(s[0])>=1 and (int)(s[0])<=31:
                if (int)(s[1])>=1 and (int)(s[1])<=12:
                    if len(s[2])==4:
                        return True
                    else:
                        False
                else:
                    False
            else:
                False
        else:
            False
    else:
        False
##    for i in datee:
##        if i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9':
##            count+=1
##        if i=='/':
##            countslash+=1
##    if len(datee)==(count+countslash) and (len(datee)==10 or len(datee)==9 or len(datee)==8):
##        return True
##    else:
##        return False


def check_seat_mob_age(num):
    return num.isnumeric()

def sure():
    messagebox.askyesno("bus confirmation", "Are you sure you want to book the bus?")
    
    
def checkFilling():
    if len(goingTo.get())==0:
        messagebox.showerror('Value missing','Enter Boarding')
    elif len(destination.get())==0:
        messagebox.showerror('Value missing','Enter Destination')
    elif len(Jdate.get())==0:
        messagebox.showerror('Value missing','Enter Date')
    else:
        if checkTo(goingTo.get())==True and checkFrom(destination.get())==True and checkDate(Jdate.get())==True:
            showDetails()
        else:
            messagebox.showerror('Invalid Entry',"Enter Details Properly")

def checking(name_ent,seats_ent,mobile_ent,age_ent):
    if(len(name_ent.get())==0 and len(mobile_ent.get())<10 and len(age_ent.get())==0 and len(seats_ent.get())==0):
        messagebox.showerror('Invalid Entry',"Enter Details Properly")
    else:
        if checkTo(name_ent.get())==True and check_seat_mob_age(seats_ent.get())==True and check_seat_mob_age(mobile_ent.get())==True and check_seat_mob_age(age_ent.get())==True:
            sure()
        else:
            messagebox.showerror('Invalid Entry',"Enter Details Properly")


def showDetails():
    select_text = Label(root, text = "Select Bus", fg = "green",pady=h//30)
    select_text.grid(row = 4, column=0)

    opt_text = Label(root, text = "Operator", fg = "green")
    opt_text.grid(row = 4, column=1)

    type_text = Label(root, text = "Bus Type", fg = "green")
    type_text.grid(row = 4, column=2)

    available_text = Label(root, text = "Available/Capacity", fg = "green")
    available_text.grid(row = 4, column=3)

    fare_text = Label(root, text = "Fare", fg = "green")
    fare_text.grid(row = 4, column=4)

    book_button = Button(root, text="Proceed to Book", bg = "lightgreen", command = book)
    book_button.grid(row =5 , column= 4, pady=h//50)


def book():
     fill_label = Label(root, text = "Fill Passenger Details to book the bus ticket" , fg = 'red' , bg = 'lightblue', font = 'Arian 14 bold')
     fill_label.grid(row = 6, column = 0, columnspan = 8,pady=h//30)

     name_text = Label(root, text = "Name")
     name_text.grid(row = 7, column=0)

     name_ent = Entry(root)
     name_ent.grid(row =7, column=1)

     Label(root,text='Gender',font='Arial 13').grid(row=7,column=2)
     genders=["MALE","FEMALE"]
     gender_ent=StringVar()
     gender_ent.set(genders[0])
     gender_ent_2=OptionMenu(root,gender_ent,*genders)
     gender_ent_2.grid(row=7,column=3)

     seats_text = Label(root, text = "No of Seats")
     seats_text.grid(row = 7, column=4)

     seats_ent = Entry(root)
     seats_ent.grid(row =7, column=5)

     mobile_text = Label(root, text = "Mobile No")
     mobile_text.grid(row = 7, column=6)

     mobile_ent = Entry(root)
     mobile_ent.grid(row =7, column=7)

     age_text = Label(root, text = "Age")
     age_text.grid(row = 8, column=4,pady=h//50)

     age_ent = Entry(root)
     age_ent.grid(row =8, column=5)

     book_button = Button(root, text = "Book Seat", bg ="lightgreen", command = lambda :[checking(name_ent,seats_ent,mobile_ent,age_ent)])
     book_button.grid(row = 8, column=7)



#to
Label(root,text="To:").grid(row=3,column=0)
goingTo=Entry(root)
goingTo.grid(row=3,column=1)

#from
Label(root,text="From:").grid(row=3,column=2)
destination=Entry(root)
destination.grid(row=3,column=3)

#Journey date
Label(root,text="Journey Date:").grid(row=3,column=4)
Label(root,text="(DD/MM/YYYY)").grid(row=4,column=5)

Jdate=Entry(root)
Jdate.grid(row=3,column=5)

#Buttons
Button(root,text="Show Bus",bg="pale green",command=checkFilling).grid(row=3,column=6)
#Button(root,image=home_Image).grid(row=3,column=7)

# main_3()

