import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class Registration:
    def __init__(self,root):
        self.root = root
        self.root.title("Patient Registration System")
        self.root.geometry('1350x750+0+0')
        self.root.configure(background = 'black')


        ## we will take live time date by using time module

        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime('%d/%m/%y'))

        Ref = StringVar()
        Mobile_no = StringVar()
        Pincode = StringVar()
        Address = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()

        ## this var1,2,3,4,5 are for combobox
        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = StringVar()
        var5 = IntVar()           # we will keep as int bcz we will keep here numerical value

        Membership = StringVar()
        Membership.set('0')      # when membership checkbox is unclicked or reset has been done it will automatically set as zero(0)

        #################### function ####################################

        def exitbtt():
            exitbtt = tkinter.messagebox.askyesno("Member Registration Form",'Are you sure you want to exit ?')
            if exitbtt > 0:
                root.destroy()
            else:
                self.newWindow = Toplevel(self.master)
                self.app = Registration(self.newWindow)
                return

        def resetbtt():
            Firstname.set('')
            Ref.set('')
            Mobile_no.set('')
            Pincode.set('')
            Address.set('')
            Lastname.set('')

            var1.set('')
            var2.set('')
            var3.set('')
            var4.set('')
            var5.set('')

            Membership.set('0')
            member_gendercmb.current(0)
            member_id_proofcmb.current(0)
            member_memtypecmb.current(0)
            member_paymentwithcmb.current(0)
            member_membershiptxt.configure(state = DISABLED)

        def reeesetbtt():
            reeesetbtt = tkinter.messagebox.askokcancel('Member Registration Form','You want to add as new Record')
            if reeesetbtt > 0:
                resetbtt()
            elif reeesetbtt <= 0:
                resetbtt()
                detail_labeltxt.delete('1.0',END)
                return

        def Reference_number():
            ranumber = random.randint(10000,9999999)
            randomnumber = str(ranumber)
            Ref.set(randomnumber)

        def membership_fees():

            if(var5.get() == 1):     # when checkbox is clicked
                member_membershiptxt.configure(state = NORMAL)
                item = float(15000)   # it is random price of membership plan you can change according to you
                Membership.set(str(item)+ 'Rs')
            elif(var5.get() == 0):
                # when unchecked
                member_membershiptxt.configure(state = DISABLED)
                Membership.set('0')

        def Receipt():
            Reference_number()
            detail_labeltxt.insert(END,'\t' +Date_of_Registration.get() + "        \t" + Ref.get()+ "\t\t"+
            Firstname.get()+'           \t'+ Lastname.get()+'       \t'+Mobile_no.get()+'\t'+
            '\t'+ Address.get() +'     \t\t'+ Pincode.get()+'     \t'+member_gendercmb.get()+
            '\t\t'+Membership.get() + '\n')



        ################################ TITLE #################################
        title = Label(self.root, text='Member Registration Form', font=("monotype corsive",30,'bold'),bd=5,
                      relief = GROOVE,bg='#E6005C',fg='#000000')
        title.pack(side=TOP, fill = X)

        ################ Member Frame ############################
        Manage_Frame = Frame(self.root,bd = 4,relief = RIDGE,bg = '#001a66')
        Manage_Frame.place(x=20,y=100,width=450,height = 630)

        ############### text, label, comboboxes in manage frame ############
        Cus_title = Label(Manage_Frame,text="Customer Details",font = ('arial',20,'bold'),bg = '#001a66',fg='white')
        Cus_title.grid(row = 0, columnspan = 2, pady = 5)

        member_datelbl = Label(Manage_Frame,text='Date',font=('arial',15,'bold'),bg = '#001a66',fg='white')
        member_datelbl.grid(row=1,column=0,pady=5,padx=10,sticky='w')

        member_datetxt = Entry(Manage_Frame,font = ('arial',15,'bold'), textvariable=Date_of_Registration)
        member_datetxt.grid(row=1,column=1,pady=5,padx=10,sticky='w')


        member_reflbl = Label(Manage_Frame,text = 'Reference ID',font=('arial',15,'bold'),bg = '#001a66',fg = 'white')
        member_reflbl.grid(row=2,column=0,pady=5,padx=10,sticky='w')

        member_reftxt = Entry(Manage_Frame, font=('arial', 15, 'bold'), state=DISABLED,text = Ref)
        member_reftxt.grid(row=2, column=1, pady=5, padx=10, sticky='w')


        member_fnamelbl = Label(Manage_Frame, text='First Name', font=('arial', 15, 'bold'), bg='#001a66', fg='white')
        member_fnamelbl.grid(row=3, column=0, pady=5, padx=10, sticky='w')

        member_fnametxt = Entry(Manage_Frame, font=('arial', 15, 'bold'), textvariable= Firstname)
        member_fnametxt.grid(row=3, column=1, pady=5, padx=10, sticky='w')

        member_lnamelbl = Label(Manage_Frame, text='Last Name', font=('arial', 15, 'bold'), bg='#001a66', fg='white')
        member_lnamelbl.grid(row=4, column=0, pady=5, padx=10, sticky='w')

        member_lnametxt = Entry(Manage_Frame, font=('arial', 15, 'bold'), textvariable= Lastname)
        member_lnametxt.grid(row=4, column=1, pady=5, padx=10, sticky='w')

        member_mobilelbl = Label(Manage_Frame, text='Mobile No', font=('arial', 15, 'bold'), bg='#001a66', fg='white')
        member_mobilelbl.grid(row=5, column=0, pady=5, padx=10, sticky='w')

        member_mobiletxt = Entry(Manage_Frame, font=('arial', 15, 'bold'), textvariable= Mobile_no)
        member_mobiletxt.grid(row=5, column=1, pady=5, padx=10, sticky='w')

        member_addresslbl = Label(Manage_Frame, text='Address', font=('arial', 15, 'bold'), bg='#001a66', fg='white')
        member_addresslbl.grid(row=6, column=0, pady=5, padx=10, sticky='w')

        member_addresstxt = Entry(Manage_Frame, font=('arial', 15, 'bold'), textvariable=Address)
        member_addresstxt.grid(row=6, column=1, pady=5, padx=10, sticky='w')

        member_pincodelbl = Label(Manage_Frame, text='Pincode', font=('arial', 15, 'bold'), bg='#001a66', fg='white')
        member_pincodelbl.grid(row=7, column=0, pady=5, padx=10, sticky='w')

        member_pincodetxt = Entry(Manage_Frame, font=('arial', 15, 'bold'), textvariable=Pincode)
        member_pincodetxt.grid(row=7, column=1, pady=5, padx=10, sticky='w')


        member_genderlbl = Label(Manage_Frame, text='Gender', font=('arial', 15, 'bold'), bg='#001a66', fg='white')
        member_genderlbl.grid(row=8, column=0, pady=5, padx=10, sticky='w')

        member_gendercmb = ttk.Combobox(Manage_Frame, text = var4, state = 'readonly', font=('arial',15,'bold'),width=19)
        member_gendercmb['values'] = ("",'Male','Female','Other')
        member_gendercmb.current(0)   # when nothing it will be set as empty which we have given at index 0
        member_gendercmb.grid(row = 8, column = 1, pady= 5, padx = 10, sticky = 'w')


        member_id_prooflbl = Label(Manage_Frame, text='ID Proof', font=('arial', 15, 'bold'), bg='#001a66', fg='white')
        member_id_prooflbl.grid(row=9, column=0, pady=5, padx=10, sticky='w')

        member_id_proofcmb = ttk.Combobox(Manage_Frame, text=var3, state='readonly', font=('arial', 15, 'bold'), width=19)
        member_id_proofcmb['values'] = ("", 'Adhaar Card', 'Passport', 'Driving License', 'Pan Card','Student ID')
        member_id_proofcmb.current(0)  # when nothing it will be set as empty which we have given at index 0
        member_id_proofcmb.grid(row=9, column=1, pady=5, padx=10, sticky='w')


        member_memtypelbl = Label(Manage_Frame, text='Member Type', font=('arial', 15, 'bold'), bg='#001a66', fg='white')
        member_memtypelbl.grid(row=10, column=0, pady=5, padx=10, sticky='w')

        member_memtypecmb = ttk.Combobox(Manage_Frame, text=var2, state='readonly', font=('arial', 15, 'bold'),
                                          width=19)
        member_memtypecmb['values'] = ("", 'Ayushman Card', 'Insurance', 'Pay Immediately', 'Pay when leaving')
        member_memtypecmb.current(0)  # when nothing it will be set as empty which we have given at index 0
        member_memtypecmb.grid(row=10, column=1, pady=5, padx=10, sticky='w')



        member_paymentwithlbl = Label(Manage_Frame, text='Payment Method', font=('arial', 15, 'bold'), bg='#001a66',
                                  fg='white')
        member_paymentwithlbl.grid(row=11, column=0, pady=5, padx=10, sticky='w')

        member_paymentwithcmb = ttk.Combobox(Manage_Frame, text=var1, state='readonly', font=('arial', 15, 'bold'),
                                         width=19)
        member_paymentwithcmb['values'] = ("", 'Cash', 'Debit Card - Rupay', 'Debit Card - Visa','Debit Card - Mastercard','Credit Card','Phonepe','GooglePay','PayTm')
        member_paymentwithcmb.current(0)  # when nothing it will be set as empty which we have given at index 0
        member_paymentwithcmb.grid(row=11, column=1, pady=5, padx=10, sticky='w')



        member_membership = Checkbutton(Manage_Frame,text='Membership Fees',variable=var5,onvalue=1,
                                        offvalue=0, font=('arial', 15, 'bold'),bg="#001a66",fg='white', command=membership_fees)
        member_membership.grid(row=12,column=0,sticky='w')
        member_membershiptxt = Entry(Manage_Frame,font=('arial', 15, 'bold'),state = DISABLED, justify = RIGHT,textvariable = Membership)
        member_membershiptxt.grid(row=12, column =1, pady=5,padx=10,sticky = 'w')



        ################# Detail Frame #########################
        detail_frame = Frame(self.root, relief = RIDGE, bg = '#001a66')
        detail_frame.place(x=500,y=100,width=820,height=630)

        detail_label = Label(detail_frame,font=('arial', 11, 'bold'),pady =10, padx=2,width=95,
                             text='Date\t Ref Id\t Firstname    Lastname    Mobile No         Address         Pincode    Gender     Membership')
        detail_label.grid(row = 0,column=0,columnspan=4,sticky='w')
        detail_labeltxt = Text(detail_frame, width = 123, height = 34, font=('arial',10))
        detail_labeltxt.grid(row=1,column=0,columnspan=4)


        ################### we will add button in detail frame #############################

        receiptbtn = Button(detail_frame, padx = 15, bd=5, font=('arial',12,'bold'), bg='#ff9966', width=20, text='Receipt',command=Receipt)
        receiptbtn.grid(row = 2,column = 0)

        resetbtn = Button(detail_frame, padx=15, bd=5, font=('arial', 12, 'bold'), command= reeesetbtt, bg='#ff9966', width=20,
                            text='Reset')
        resetbtn.grid(row=2, column=1)

        exitbtn = Button(detail_frame, padx=15, bd=5, font=('arial', 12, 'bold'),command=exitbtt, bg='#ff9966', width=20,
                            text='Exit')
        exitbtn.grid(row=2, column=2)


if __name__ == '__main__':
    root = Tk()
    app = Registration(root)
    root.mainloop()


