from tkinter import *

class Login:
    """ This class is for creating a login window """
    def __init__(self) :
        self.root = Tk()
        self.root.title('Login')
        self.root.geometry('626x384')
        self.root.resizable(0, 0)
        self.login_stringvar = StringVar()
        self.login_usename_stringvar = StringVar()
        self.login_password_stringvar = StringVar()


        # =============================Photo background===============================
        self.photoimage = PhotoImage(file='./image/bg.for login3.png/')
        self.lb_photo = Label(self.root, image=self.photoimage)
        self.lb_photo.pack()
        # ================================mainFrame================================
        self.main_frame = Frame(self.root, bg='#d5ecf5')
        self.main_frame.place(x=162, y=10, width=300, height=364)

        #=====================================images================================

        self.logImage = PhotoImage(file='./image/wo_man4.png')
        self.logImage2 = PhotoImage(file='./image/personriz_2.png')
        self.passimage = PhotoImage(file='./image/ghofleriz_2.png')

        # ===================  Labels for left and right   -->  label_User    logimage    label_Login  ==========================
        self.lb_user = Label(self.main_frame, text='User', font=('comic sans ms', 20, 'bold'), bg='#d5ecf5', fg='#000066')
        self.lb_user.place(x=20, y=30)
        self.lb_login = Label(self.main_frame, text='Login', font=('comic sans ms', 20, 'bold'), bg='#d5ecf5', fg='#000066')
        self.lb_login.place(x=220, y=30)
        # ==== logimage ====
        self.lb_logimage = Label(self.main_frame, image=self.logImage, bg='#d5ecf5') 
        self.lb_logimage.place(x=92, y=0)
        # =============  label for entry(username  and  password) ==================================
        self.lb_username = Label(self.main_frame, text='username', font=('comic sans ms', 10), fg='#0000b3', bg='#d5ecf5')
        self.lb_username.place(x=0, y=120)

        self.lb_pass = Label(self.main_frame, text='password', font=('comic sans ms', 10), fg='#0000b3', bg='#d5ecf5')
        self.lb_pass.place(x=0, y=169)
        # ========================= label for question  ===================================
        self.lb_signup = Label(
            self.main_frame, text='Dont have an account?', font=('comic sans ms', 10), bg='#d5ecf5', fg='#0000cc')
        self.lb_signup.place(x=5, y=330)
        
        # =================== label for Entrie's images(icon) ====================================

        self.lb_logimage2 = Label(self.main_frame, image=self.logImage2, bg='#ffffff', height=21)
        self.lb_logimage2.place(x=5, y=141)
        self.lb_passimage = Label(self.main_frame, image=self.passimage, bg='#ffffff')
        self.lb_passimage.place(x=5, y=192)

        #================================= Entries===============================

        self.name_entry = Entry(self.main_frame, font=('comic sans ms', 12), width=25, textvariable=self.login_usename_stringvar)
        self.name_entry.place(x=30, y=140)
        self.pass_entry = Entry(self.main_frame, font=('comic sans ms', 12), width=25, show='*', textvariable=self.login_password_stringvar)
        self.pass_entry.place(x=30, y=190)

        # ============= label for label_login_stringvar =================================
        self.label_stringvar = Label(self.main_frame, textvariable=self.login_stringvar, bg='#d5ecf5', fg='red', width=27,
                                           font=('comic sans ms', 11))
        self.label_stringvar.place(x=32, y=225)
        #================================ Buttons===================================
        self.btn_log = Button(
            self.main_frame, text='LOGIN', font=('comic sans ms', 11), background='#0488c9', foreground='#ffffff',
            activebackground='#ffffff', activeforeground='#0488c9', command=self.login_command)
        self.btn_log.place(x=30, y=260, width=250)

        self.btn_forgotpass = Button(
            self.main_frame, text='forgot your password?', background='#d5ecf5', foreground='#ccccff', relief=FLAT,
            activebackground='#d5ecf5', activeforeground='#733603', command=self.forgot_username_page)
        self.btn_forgotpass.place(x=155, y=300)

        self.btn_signup = Button(
            self.main_frame, text='Sign up!', background='#d5ecf5', foreground='#660066', relief=FLAT,
            activebackground='#ff4dff', activeforeground='#ff4dff', font=('comic sans ms', 11),
            command=self.sign_up_page)
        self.btn_signup.place(x=165, y=326)

# ============================================ Button.binds ===================================================================

        self.btn_signup.bind('<Motion>', self.cursor_on_sign_up)
        self.main_frame.bind('<Motion>', self.cursor_on_main_frame)
        self.btn_log.bind('<Motion>', self.cursor_on_btn_log_in)
        self.btn_forgotpass.bind('<Motion>', self.cursor_on_btn_forgot_pass)