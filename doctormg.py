import time
import random
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


class Doctor():
    def __init__(self,root):
        self.root = root
        self.root.title('Doctor Management System')
        self.root.geometry('1700x900+0+0')
        self.root.configure(background = 'black')


        ############################### we will Declare all function  together #######################3
        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime('%d/%m/%y'))

        DrID = StringVar()
        Drname = StringVar()
        DateofBirth= StringVar()
        Spes = StringVar()
        GovtPri = StringVar()
        Surgeries = StringVar()
        Experiences = StringVar()
        Nurses = StringVar()
        DrMobile = StringVar()
        PtName = StringVar()
        Apptime = StringVar()
        PtAge = StringVar()
        PatientAdrress = StringVar()
        PtMobile = StringVar()
        Disease = StringVar()
        Case = StringVar()
        BenefitCard = StringVar()

        def exitbtn():
            exitbtn = tkinter.messagebox.askyesno('Doctor Management System','Are you sure you want to exit ?')
            if exitbtn > 0:
                root.destroy()
                return

        def resetfunc():
            DrID.set('')
            Drname.set('')
            DateofBirth.set('')
            Spes.set('')
            GovtPri.set('')
            Surgeries.set('')
            Experiences.set('')
            Nurses.set('')
            DrMobile.set('')
            PtName.set('')
            Apptime.set('')
            PtAge.set('')
            PatientAdrress.set('')
            PtMobile.set('')
            Disease.set('')
            Case.set('')
            BenefitCard.set('')
            TextPrescription.delete('1.0',END)
            return

        def deletefunc():
            DrID.set('')
            Drname.set('')
            DateofBirth.set('')
            Spes.set('')
            GovtPri.set('')
            Surgeries.set('')
            Experiences.set('')
            Nurses.set('')
            DrMobile.set('')
            PtName.set('')
            Apptime.set('')
            PtAge.set('')
            PatientAdrress.set('')
            PtMobile.set('')
            Disease.set('')
            Case.set('')
            BenefitCard.set('')
            TextPrescription.delete('1.0', END)
            TextPrescriptionData.delete('1.0', END)
            return

        def Patient_idFunc():
            ranumber = random.randint(10000,999999)
            randomnumber = str(ranumber)
            DrID.set(randomnumber)

        def prescriptiondatafunc():
            Patient_idFunc()
            TextPrescriptionData.insert(END,Date_of_Registration.get()+'\t'+DrID.get()+'\t'+Drname.get()+'\t\t'
                                        +DateofBirth.get()+'\t\t'+Spes.get()+'\t\t'+GovtPri.get()+'\t\t'+
                                        Surgeries.get()+'\t\t'+Experiences.get()+'\t\t'+Nurses.get()+'\t'+DrMobile.get()+'\t\t'+
                                        PtName.get()+'\t\t'+Case.get()+'\t'+PtAge.get()+'\n')
            return

        def prescriptionfunc():
            Patient_idFunc()
            TextPrescription.insert(END,'Date: \t\t'+Date_of_Registration.get()+'\n')
            TextPrescription.insert(END, 'Patient Name: \t\t' + PtName.get() + '\n')
            TextPrescription.insert(END, 'Appointment Time: \t\t' + Apptime.get() + '\n')
            TextPrescription.insert(END, 'Age: \t\t' + PtAge.get() + '\n')
            TextPrescription.insert(END, 'Address: \t\t' + PatientAdrress.get() + '\n')
            TextPrescription.insert(END, 'Disease: \t\t' + Disease.get() + '\n')
            TextPrescription.insert(END, 'Case: \t\t' + Case.get() + '\n')
            TextPrescription.insert(END, 'Benefit Card: \t\t' + BenefitCard.get() + '\n')
            TextPrescription.insert(END, 'To meet Dr.: \t\t' + Drname.get() + '\n')
            TextPrescription.insert(END, 'Dr. Mobile No.: \t\t' + DrMobile.get() + '\n')
            return

        ############################### Title Label ##################################
        title = Label(self.root, text = "Doctor Management System", font =('monotype corsive',42,'bold'),bd=5,
                      relief=GROOVE, bg="#b7d8d6", fg='black')
        title.pack(side = TOP ,fill = X)

        ############### Frame
        Manage_Frame = Frame(self.root , width = 1510, height=400, bd=5,relief=RIDGE,bg='#789e9e')
        Manage_Frame.place(x=10,y=80)

        Button_Frame = Frame(self.root, width=1510, height=55, bd=4, relief=RIDGE, bg='#eef3db')
        Button_Frame.place(x=10, y=460)

        Data_Frame = Frame(self.root, width=1510, height=270, bd=4, relief=RIDGE, bg='#eef3db')
        Data_Frame.place(x=10, y=510)

        Data_FrameLeft = LabelFrame(Manage_Frame, width = 1050, text='General Information',
        font=('arial',20,'italic bold'),height = 390,bd=7,pady=1,relief=RIDGE,bg='#789e9e')
        Data_FrameLeft.pack(side = LEFT)

        Data_Framedata = LabelFrame(Data_Frame, width=1050, text='Doctor\'s Details',
                                    font=('arial', 12, 'italic bold'), height=390, bd=7, relief=RIDGE,
                                    bg='#b7d8d6')
        Data_Framedata.pack(side=LEFT)

        Data_FrameRight = LabelFrame(Manage_Frame, width=1050, text='Patient\'s Information',
                                    font=('arial', 15, 'italic bold'), height=390, bd=7, relief=RIDGE,
                                    bg='#789e9e')
        Data_FrameRight.pack(side=RIGHT)


        ####################### Doctor's ID
        DrIdlbl = Label(Data_FrameLeft, font = ('arial',12,'bold'),width=20,text='Doctor ID',bg ='#789e9e')
        DrIdlbl.grid(row = 0,column =0, padx=10,pady=5,sticky=W)
        DrIdtxt = Entry(Data_FrameLeft, font=('arial',12,'bold'),width=27,state=DISABLED,textvariable = DrID)
        DrIdtxt.grid(row=0, column= 1,padx= 10,pady=5,sticky=E)

        DrNamelbl = Label(Data_FrameLeft, font=('arial', 12, 'bold'), width=20, text='Doctor Name', bg='#789e9e')
        DrNamelbl.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        DrNametxt = Entry(Data_FrameLeft, font=('arial', 12, 'bold'), width=27, textvariable=Drname)
        DrNametxt.grid(row=1, column=1, padx=10, pady=5, sticky=E)

        DateofBirthlbl = Label(Data_FrameLeft, font=('arial', 12, 'bold'), width=20, text='Date of Birth', bg='#789e9e')
        DateofBirthlbl.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        DateofBirthtxt = Entry(Data_FrameLeft, font=('arial', 12, 'bold'), width=27, textvariable=DateofBirth)
        DateofBirthtxt.grid(row=2, column=1, padx=10, pady=5, sticky=E)

        Speslbl = Label(Data_FrameLeft, font=('arial', 12, 'bold'), width=20, text='Specialisation', bg='#789e9e')
        Speslbl.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        Spestxt = Entry(Data_FrameLeft, font=('arial', 12, 'bold'), width=27,  textvariable=Spes)
        Spestxt.grid(row=3, column=1, padx=10, pady=5, sticky=E)

        GovtPrilbl = Label(Data_FrameLeft, font=('arial', 12, 'bold'), width=20, text='Govt/Private', bg='#789e9e')
        GovtPrilbl.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        GovtPricmb = ttk.Combobox(Data_FrameLeft, textvariable = GovtPri, width=25,state='readonly',font=('arial',12,'bold'))
        GovtPricmb['values'] = ('', 'Government', 'Private')
        GovtPricmb.current(0)
        GovtPricmb.grid(row = 4, column = 1, padx = 10, pady=5, sticky = E)

        Surgerieslbl = Label(Data_FrameLeft, font=('arial', 12, 'bold'), width=20, text='Surgeries', bg='#789e9e')
        Surgerieslbl.grid(row=5, column=0, padx=10, pady=5, sticky=W)
        Surgeriestxt = Entry(Data_FrameLeft, font=('arial', 12, 'bold'), width=27, textvariable=Surgeries)
        Surgeriestxt.grid(row=5, column=1, padx=10, pady=5, sticky=E)

        Experienceslbl = Label(Data_FrameLeft, font=('arial', 12, 'bold'), width=20, text='Experiences', bg='#789e9e')
        Experienceslbl.grid(row=6, column=0, padx=10, pady=5, sticky=W)
        Experiencestxt = Entry(Data_FrameLeft, font=('arial', 12, 'bold'), width=27, textvariable=Experiences)
        Experiencestxt.grid(row=6, column=1, padx=10, pady=5, sticky=E)

        Nurseslbl = Label(Data_FrameLeft, font=('arial', 12, 'bold'), width=20, text='Nurse under Dr', bg='#789e9e')
        Nurseslbl.grid(row=7, column=0, padx=10, pady=5, sticky=W)
        Nursestxt = Entry(Data_FrameLeft, font=('arial', 12, 'bold'), width=27, textvariable=Nurses)
        Nursestxt.grid(row=7, column=1, padx=10, pady=5, sticky=E)

        DrMobilelbl = Label(Data_FrameLeft, font=('arial', 12, 'bold'), width=20, text='Doctor Mobile No.', bg='#789e9e')
        DrMobilelbl.grid(row=8, column=0, padx=10, pady=5, sticky=W)
        DrMobiletxt = Entry(Data_FrameLeft, font=('arial', 12, 'bold'), width=27, textvariable=DrMobile)
        DrMobiletxt.grid(row=8, column=1, padx=10, pady=5, sticky=E)

        Datelbl = Label(Data_FrameLeft, font =('arial',12,'bold'),width = 20, text='Date',padx=2,bg='#789e9e')
        Datelbl.grid(row = 0, column = 2,padx=10,pady=5,sticky=W)
        Datetxt = Entry(Data_FrameLeft, font=('arial',12,'bold'),width=27,textvariable=Date_of_Registration)
        Datetxt.grid(row = 0,column=3,padx=10,pady=5,sticky=E)

        PtNamelbl = Label(Data_FrameLeft, font=('arial', 12, 'bold'), width=20, text='Patient Name', padx=2, bg='#789e9e')
        PtNamelbl.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        PtNametxt = Entry(Data_FrameLeft, font=('arial', 12, 'bold'), width=27, textvariable=PtName)
        PtNametxt.grid(row=1, column=3, padx=10, pady=5, sticky=E)

        Apptimelbl = Label(Data_FrameLeft, font=('arial', 12, 'bold'), width=20, text='Appointment Time', padx=2, bg='#789e9e')
        Apptimelbl.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        Apptimetxt = Entry(Data_FrameLeft, font=('arial', 12, 'bold'), width=27, textvariable=Apptime)
        Apptimetxt.grid(row=2, column=3, padx=10, pady=5, sticky=E)

        PtAgelbl = Label(Data_FrameLeft, font=('arial', 12, 'bold'), width=20, text='Patient Age', padx=2, bg='#789e9e')
        PtAgelbl.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        PtAgetxt = Entry(Data_FrameLeft, font=('arial', 12, 'bold'), width=27, textvariable=PtAge)
        PtAgetxt.grid(row=3, column=3, padx=10, pady=5, sticky=E)

        PatientAdrresslbl = Label(Data_FrameLeft, font=('arial', 12, 'bold'), width=20, text='Patient Adrress', padx=2, bg='#789e9e')
        PatientAdrresslbl.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        PatientAdrresstxt = Entry(Data_FrameLeft, font=('arial', 12, 'bold'), width=27, textvariable=PatientAdrress)
        PatientAdrresstxt.grid(row=4, column=3, padx=10, pady=5, sticky=E)

        PtMobilelbl = Label(Data_FrameLeft, font=('arial', 12, 'bold'), width=20, text='Patient Mobile Number', padx=2, bg='#789e9e')
        PtMobilelbl.grid(row=5, column=2, padx=10, pady=5, sticky=W)
        PtMobiletxt = Entry(Data_FrameLeft, font=('arial', 12, 'bold'), width=27, textvariable=PtMobile)
        PtMobiletxt.grid(row=5, column=3, padx=10, pady=5, sticky=E)

        Diseaselbl = Label(Data_FrameLeft, font=('arial', 12, 'bold'), width=20, text='Disease', padx=2, bg='#789e9e')
        Diseaselbl.grid(row=6, column=2, padx=10, pady=5, sticky=W)
        Diseasetxt = Entry(Data_FrameLeft, font=('arial', 12, 'bold'), width=27, textvariable=Disease)
        Diseasetxt.grid(row=6, column=3, padx=10, pady=5, sticky=E)

        Caselbl = Label(Data_FrameLeft, font=('arial', 12, 'bold'), width=20, text='Case', bg='#789e9e')
        Caselbl.grid(row=7, column=2, padx=10, pady=5, sticky=W)
        Casecmb = ttk.Combobox(Data_FrameLeft, textvariable=Case, width=25, state='readonly',
                                  font=('arial', 12, 'bold'))
        Casecmb['values'] = ('','New Case','Old Case')
        Casecmb.current(0)
        Casecmb.grid(row=7, column=3, padx=10, pady=5, sticky=E)

        BenefitCardlbl = Label(Data_FrameLeft, font=('arial', 12, 'bold'), width=20, text='BenefitCard', bg='#789e9e')
        BenefitCardlbl.grid(row=8, column=2, padx=10, pady=5, sticky=W)
        BenefitCardcmb = ttk.Combobox(Data_FrameLeft, textvariable=BenefitCard, width=25, state='readonly',
                               font=('arial', 12, 'bold'))
        BenefitCardcmb['values'] = ('', 'Ayushman Card', 'Health Insurance','Senior Citizen','Army Card')
        BenefitCardcmb.current(0)
        BenefitCardcmb.grid(row=8, column=3, padx=10, pady=5, sticky=E)


        ############################### TextPrescription #####################

        TextPrescription = Text(Data_FrameRight, font=('arial',12,'bold'),width = 55, height = 17, padx = 3,pady=5)
        TextPrescription.grid(row=0,column=0)
        TextPrescriptionData = Text(Data_Framedata, font = ('arial',12,'bold'),width=203,height =12)
        TextPrescriptionData.grid(row = 1,column = 0)

        ############################# buttons ###############################

        Prescriptionbtn = Button(Button_Frame, text='Patient Information',bg='#fe615a',activebackground = '#cc6686',
                                 font=('arial',15,'bold'),width = 22,command=prescriptionfunc)
        Prescriptionbtn.grid(row = 0,column=0,padx=15)

        DoctorDetailbtn = Button(Button_Frame, text='Doctor\'s Details', bg='#fe615a', activebackground='#cc6686',
                                 font=('arial', 15, 'bold'), width=22,command=prescriptiondatafunc)
        DoctorDetailbtn.grid(row=0, column=1, padx=15)

        Resetbtn = Button(Button_Frame, text='Reset', bg='#fe615a', activebackground='#cc6686',
                                 font=('arial', 15, 'bold'), width=22,command=resetfunc)
        Resetbtn.grid(row=0, column=2, padx=15)

        Deletebtn = Button(Button_Frame, text='Delete', bg='#fe615a', activebackground='#cc6686',
                                 font=('arial', 15, 'bold'), width=22 ,command = deletefunc)
        Deletebtn.grid(row=0, column=3, padx=15)

        Exitbtn = Button(Button_Frame, text='Exit', bg='#fe615a', activebackground='#cc6686',
                                 font=('arial', 15, 'bold'), width=22,command = exitbtn)
        Exitbtn.grid(row=0, column=4, padx=15)


        prescriptiondatarow = Label(Data_Framedata, bg='white', font=('arial',12,'bold'),
         text='Date\tDoctor Id\tDoctor Name\tDate of Birth\tSpecialisation\tGovt/Private\tSurgeries'
              '\tExperience\tNurses\tDr Mobile No.\tPatient Name\tCase\tPt.Age')
        prescriptiondatarow.grid(row=0, column=0,sticky=W)


if __name__ == '__main__':
    root = Tk()
    app = Doctor(root)
    root.mainloop()


