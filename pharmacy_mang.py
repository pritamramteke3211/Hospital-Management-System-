import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import registration
import hospital
import doctormg


def main():
    root = Tk()
    app = windows1(root)
    root.mainloop()

class windows1:
    def __init__(self,master):
        self.master = master
        self.master.title('Pharmacy Management System')
        self.master.geometry('1350x750+0+0') # x-axis, y-axis, 0, 0 are location from  topm leftmost
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.LabelTitle = Label(self.frame,text="     Pharmacy Management System      ",font = ('arial',40,'bold'),
                                bd = 10,relief = 'sunken')
        self.LabelTitle.grid(row = 0,column = 0,columnspan = 2,pady=20)

        self.Loginframe1 = Frame(self.frame, width = 1000, height= 300, bd = 10, relief = 'groove')
        self.Loginframe1.grid(row=1,column=0)

        self.Loginframe2 = Frame(self.frame, width=1000, height=100, bd=10, relief='groove')
        self.Loginframe2.grid(row=2, column=0,pady=15)

        self.Loginframe3 = Frame(self.frame, width=1000, height=200, bd=10, relief='groove')
        self.Loginframe3.grid(row=6, column=0,pady = 5)

        ## window's button
        self.button_reg = Button(self.Loginframe3,text = 'Patient Registration Window',state= DISABLED,font = ('arial',15,'bold'),
                                 command = self.Registration_window)
        self.button_reg.grid(row = 0, column = 0,padx = 10,pady = 10)

        self.button_Hosp = Button(self.Loginframe3, text='Hospital Management Window',state= DISABLED, font=('arial', 15, 'bold'),
                                 command=self.Hospital_window)
        self.button_Hosp.grid(row=0, column=1, padx=10, pady=10)

        self.button_Dr_appt = Button(self.Loginframe3, text='Dr_Appointment Window',state= DISABLED, font=('arial', 15, 'bold'),
                                 command=self.Dr_Apoint_window)
        self.button_Dr_appt.grid(row=2, column=0, padx=10, pady=10)

        self.button_med_stock = Button(self.Loginframe3, text='Medical Stock Window',state= DISABLED, font=('arial', 15, 'bold'),
                                     command=self.Medicine_stock)
        self.button_med_stock.grid(row=2, column=1, padx=10, pady=10)


        # now we will make user name and password frame

        self.LabelUsername = Label(self.Loginframe1,text = "User Name",font = ('arial',20,'bold'),bd=3)
        self.LabelUsername.grid(row = 0, column = 0)

        self.textUsername = Entry(self.Loginframe1,font = ('arial',20,'bold'), bd=3, textvariable = self.Username)
        self.textUsername.grid(row = 0, column = 1, padx = 40, pady = 15)

        self.LabelPassword = Label(self.Loginframe1, text="Password",font = ('arial', 20, 'bold'), bd=3)
        self.LabelPassword.grid(row=1, column=0)

        self.textPassword = Entry(self.Loginframe1, font=('arial', 20, 'bold'), show='*', bd=3, textvariable=self.Password)
        self.textPassword.grid(row=1, column=1, padx = 40, pady = 15)

        # login reset and exit  button
        self.button_login = Button(self.Loginframe2, text='Login', width=20, font=('arial',18,'bold'),
                                   command=self.login_system)
        self.button_login.grid(row = 0, column=0 ,padx = 10,pady = 10)

        self.button_reset = Button(self.Loginframe2, text='Reset', width=20, font=('arial', 18, 'bold'),
                                   command=self.reset_btn)
        self.button_reset.grid(row=0, column=3, padx=10, pady=10)

        self.button_Exit = Button(self.Loginframe2, text='Exit', width=20, font=('arial', 18, 'bold'),
                                   command=self.Exit_btn)
        self.button_Exit.grid(row=0, column=6, padx=10, pady=10)

    def login_system(self):
        user = self.Username.get()
        pswd = self.Password.get()

        if(user == str('admin') and (pswd == str("admin"))):
            self.button_reg.config(state = NORMAL)
            self.button_Hosp.config(state = NORMAL)
            self.button_Dr_appt.config(state = NORMAL)
            self.button_med_stock.config(state = NORMAL)
        else:
            tkinter.messagebox.askyesno('Pharmacy Management System', 'You have entered an invalid user name or password')

            # if user name or password is incorrect it will be in its disabled state
            self.button_reg.config(state=DISABLED)
            self.button_Hosp.config(state=DISABLED)
            self.button_Dr_appt.config(state=DISABLED)
            self.button_med_stock.config(state=DISABLED)

            self.Username.set('')
            self.Password.set('')
            self.textUsername.focus()

    def reset_btn(self):
        # because when we will reset still we have't given correct user id and password
        self.button_reg.config(state=DISABLED)
        self.button_Hosp.config(state=DISABLED)
        self.button_Dr_appt.config(state=DISABLED)
        self.button_med_stock.config(state=DISABLED)

        self.Username.set('')
        self.Password.set('')
        self.textUsername.focus()

    def Exit_btn(self):
        self.Exit_btn = tkinter.messagebox.askyesno('Pharmacy Management System','Are you sure you want to exit?')
        if self.Exit_btn > 0:
            # we will close that master screen
            self.master.destroy()
            return


    # first we will define all our window
    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = registration.Registration(self.newWindow)

    def Hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = hospital.Hospital(self.newWindow)

    def Dr_Apoint_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = doctormg.Doctor(self.newWindow)

    def Medicine_stock(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows5(self.newWindow)






class windows4:
    def __init__(self,master):
        self.master = master
        self.master.title('Doctor Management System')
        self.master.geometry('1350x750+0+0') # x-axis, y-axis, 0, 0 are location from  topm leftmost
        self.frame = Frame(self.master)
        self.frame.pack()

class windows5:
    def __init__(self,master):
        self.master = master
        self.master.title('Medicine System')
        self.master.geometry('1350x750+0+0') # x-axis, y-axis, 0, 0 are location from  topm leftmost
        self.frame = Frame(self.master)
        self.frame.pack()


if __name__ == '__main__':
    main()