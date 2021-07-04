from tkinter import *
import sqlite3

class RestartPasswordPage:
    def restart_password_page(self):
        conn = sqlite3.connect("Login.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM loginpage WHERE username = ? OR password = ?",
                    (self.forgot_username.get(), self.forgot_username.get())
                    )
        self.users = cur.fetchall()
        conn.close()
        self.match_pass.set('')
        if self.users != []:
            for user in self.users:   #the users is list and user is tuple into the users 
                if self.forgot_username.get() == user[0]:  # thse user[0] is username and user[1] is password
                    self.forgot_label_username_stringvar.set('')

                    # ==============================create window for restart password=====
                    self.window_restart_pass = Toplevel()
                    self.window_restart_pass.title('Restart password')
                    self.window_restart_pass.geometry('400x380')
                    self.window_restart_pass.resizable(0, 0)

                    #============ PhotoImage and label for background ============================
                    self.photo_restart_pass = PhotoImage(file='./image/bg_for_lofpag4.png')
                    self.lbl_photo_restart_pass_page = Label(self.window_restart_pass, image=self.photo_restart_pass)
                    self.lbl_photo_restart_pass_page.pack()
                    self.lbl_photo_restart_pass_page.bind('<Motion>', self.cursor_on_mainframe_restart)
                    #======================main Frame=============================
                    self.main_frame_restartpass = Frame(self.lbl_photo_restart_pass_page, bg='#fafdff')
                    self.main_frame_restartpass.place(x=50, y=25, width=300, height=320)
                    # ====================topframe into the mainframe===================
                    self.top_frame = Frame(self.main_frame_restartpass, bg='#ed6bd4', relief=SUNKEN, bd=5)
                    self.top_frame.place(width=300, height=90)
                    #====================bottomframe into the mainframe=================
                    self.bottom_frame = Frame(self.main_frame_restartpass, bg='#74bcf7', relief=SUNKEN, bd=5)
                    self.bottom_frame.place(y=70, height=250, width=300)
                    self.bottom_frame.bind('<Motion>', self.cursor_on_bottomframe_restartpass)
                    #================= label for text in the topframe======================
                    self.lb_change_pass = Label(self.top_frame, text='Change password', font=('comic sans ms', 15),
                                           bg='#ed6bd4', fg='#3304b5')
                    self.lb_change_pass.place(x=10, y=10)
                    #===================label for entry newpassword=====================
                    self.lbl_new_pass = Label(self.bottom_frame, text='New password:', font=('comic sans ms', 11), bg='#74bcf7')
                    self.lbl_new_pass.place(x=23, y=15)
                    #===================label for entry confirmpassword=====================
                    self.lbl_confirm_pass = Label(self.bottom_frame, text='Confirm password:', font=('comic sans ms', 11),
                                             bg='#74bcf7')
                    self.lbl_confirm_pass.place(x=23, y=80)
                    # ===============label for stringvar=self.match_pass to take me text=====================
                    self.lbl_match_pass = Label(self.main_frame_restartpass, textvariable=self.match_pass, bg='#74bcf7', fg='red', width=25,
                                           font=('comic sans ms', 11))
                    self.lbl_match_pass.place(x=40, y=218)
                    #================================= Entries=======================
                    self.new_pass_entry = Entry(self.bottom_frame, font=('comic sans ms', 15))
                    self.new_pass_entry.place(x=23, y=43)
                    self.confirm_pass_entry = Entry(self.bottom_frame, font=('comic sans ms', 15), show ='*')
                    self.confirm_pass_entry.place(x=23, y=108)
                    #=================================== Button==========================
                    self.btn_new_pass = Button(
                        self.bottom_frame, text='Ok', font=('comic sans ms', 15), background='#fc0390', foreground='#ffffff',
                        relief=RAISED, activebackground='#ffffff', activeforeground='#fc0390', bd=3,
                        command=self.update)
                    self.btn_new_pass.place(x=30, y=175, width=230)
                    self.btn_new_pass.bind('<Motion>', self.cursor_on_btn_new_pass)
                    # ================= close the window user and open window_restart_pass===========
                    self.window_user.destroy()
                    self.window_restart_pass.mainloop()
                    
        elif self.forgot_username.get() == '':
            self.forgot_label_username_stringvar.set('Please enter current username')
        else:
            self.forgot_label_username_stringvar.set('User does not exist')