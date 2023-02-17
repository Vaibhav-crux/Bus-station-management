from tkinter import *
from tkinter import messagebox
root = Tk()

h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
#bus image
busImage=PhotoImage(file='.\\Bus_for_project.png')
home_Image=PhotoImage(file='.\\home.png')
Label(root,image=busImage).grid(row=0,column=0,padx=w//2.5,columnspan=3)
Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font='Arial 20 bold').grid(row=1,column=0,columnspan=3)
Label(root,text="Bus Ticket").grid(row=2,column=0,columnspan=3,pady=h//40)


final = Frame(root,relief='groove',bd=5)
final.grid(row = 3, column =0, columnspan=3)

passenger_text = Label(final, text = "Passenger: ")
passenger_text.grid(row =3, column=0)

seats_text = Label(final, text = "No of seats: ")
seats_text.grid(row =4, column=0)

age_text = Label(final, text = "Age: ")
age_text.grid(row =5, column=0)

travel_text = Label(final, text = "No of Seats: ")
travel_text.grid(row =8, column=0)

seats_text = Label(final, text = "Travel On:")
seats_text.grid(row =7, column=0)

bookingref=Label(final, text = "Booking Ref: ")
bookingref.grid(row =6, column=0)

g_text = Label(final, text = "Gender: ")
g_text.grid(row =3, column=1)

phone_text = Label(final, text = "Phone: ")
phone_text.grid(row =4, column=1)

flare_text = Label(final, text = "Flare Rs: ")
flare_text.grid(row =5, column=1)

detail_text = Label(final, text = "Bus Detail: ")
detail_text.grid(row =6, column=1)

booked_text = Label(final, text = "Booked On: ")
booked_text.grid(row =7, column=1)

point_text = Label(final, text = "Boarding Point: ")
point_text.grid(row =8, column=1)

last_text = Label(final, text = "Total amount Rs X to br paid at the time of boarding the bus",font="Arial 8 italic")
last_text.grid(row =9, column=1)

root.mainloop()
