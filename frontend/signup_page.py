from tkinter import *

class SignUp:
    def sign_up_page(self):
        # ======= set stringvar =self.sing_up_eror  and create window Registration Page ===========
        self.sing_up_eror.set('')
        self.window3 = Toplevel()
        self.window3.title('Registration Page')
        self.window3.geometry('400x380')
        self.window3.resizable(0, 0)

        #======================== PhotoImage and label for background=================================
        self.photo_sign = PhotoImage(file='./image/bg_for_sign up2.png')
        self.lbl_photo_sign_page = Label(self.window3, image=self.photo_sign)
        self.lbl_photo_sign_page.pack()

        #===========================mainFrame and top&bottom frame into the mainframe==============
        self.main_frame = Frame(self.lbl_photo_sign_page, bg='#fafdff')
        self.main_frame.place(x=50, y=25, width=300, height=300)
        self.top_frame = Frame(self.main_frame, bg='#26e7eb', relief=SUNKEN, bd=5)
        self.top_frame.place(width=300, height=60)
        self.bottom_frame = Frame(self.main_frame, bg='#d8e5f2', relief=SUNKEN, bd=5)
        self.bottom_frame.place(y=60, height=240, width=300)
        
        #================================= Label for text Rgistration into the topframe==============
        self.lbl_register = Label(
            self.top_frame, text='Registration', font=('comic sans ms', 19, 'bold'), width=300, height=60, bg='#26e7eb',
            fg='#025214')
        self.lbl_register.pack()
        
        #============= label for stringvar=self.sing_up_eror =================================
        self.lb_for_erors = Label(self.bottom_frame, textvariable=self.sing_up_eror, width=25, bg='#d8e5f2', fg='red',
                             font=('comic sans ms', 11))
        self.lb_for_erors.place(x=40, y=140)

        # ================= label for entries ========================================
        self.lbl_username = Label(self.bottom_frame, text='username:', font=('comic sans ms', 11), bg='#d8e5f2')
        self.lbl_username.place(x=23, y=15)
        self.lbl_password = Label(self.bottom_frame, text='password:', font=('comic sans ms', 11), bg='#d8e5f2')
        self.lbl_password.place(x=23, y=80)
        
        #===================================== Entries =========================
        self.usereg_entry = Entry(self.bottom_frame, font=('comic sans ms', 15))
        self.usereg_entry.place(x=23, y=43)
        self.passreg_entry = Entry(self.bottom_frame, font=('comic sans ms', 15))
        self.passreg_entry.place(x=23, y=108)
        
        #============================= Button ===============================
        self.btn_register = Button(
            self.bottom_frame, text='REGISTER', font=('comic sans ms', 15), background='#00ff0d', foreground='#ffffff',
            relief=RAISED, activebackground='#00ff0d', activeforeground='#022e0c', bd=3, command=self.sign_up_command)
        self.btn_register.place(x=30, y=165, width=230)
        self.btn_register.bind('<Motion>', self.cursor_on_btn_register)
        self.bottom_frame.bind('<Motion>', self.cursor_on_bottom_frame_registration)

        self.window3.mainloop()