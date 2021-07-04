from tkinter import *

class Forgot:
    """ This class is for creating a forgot-window to enter the username """
    def forgot_username_page(self):
        #  =============  create window and set stringvars
        self.forgot_label_username_stringvar.set('')
        self.forgot_username.set('')
        self.window_user = Toplevel()
        self.window_user.title('Forgot password')
        self.window_user.geometry('400x300')
        self.window_user.resizable(0, 0)
        # ===================Photoimage============================================
        self.photo_pass = PhotoImage(file='./image/bg_for_lofpag2.png')
        self.lbl_photo_pass_page = Label(self.window_user, image=self.photo_pass)
        self.lbl_photo_pass_page.pack()
        #============================== =====Frames==================================
        self.main_frame_forgot = Frame(self.lbl_photo_pass_page, bg='#f0cce0')
        self.main_frame_forgot.place(x=50, y=110, width=300, height=170)
        self.main_frame_forgot.bind('<Motion>', self.cursor_on_mainframe_forgot)
        # =====================Labels============================================
        self.lbl_wrong_username = Label(self.main_frame_forgot, textvariable=self.forgot_label_username_stringvar, bg='#f0cce0',
                                   font=('comic sans ms', 10), fg='red')
        self.lbl_wrong_username.place(x=50, y=75, width=200)
        self.lbl_username = Label(self.main_frame_forgot, text='username:', font=('comic sans ms', 11), bg='#f0cce0')
        self.lbl_username.place(x=23, y=15)
        # ==============================Entries====================================
        self.forget_user_entry = Entry(self.main_frame_forgot, font=('comic sans ms', 15), textvariable=self.forgot_username)
        self.forget_user_entry.place(x=23, y=43)
        #============================= Button======================================
        self.btn_for_pass = Button(
            self.main_frame_forgot, text='Restart Password', font=('comic sans ms', 14), background='#fc0390',
            foreground='#ffffff',relief=RAISED, activebackground='#ffffff', activeforeground='#fc0390', bd=3,
            command=self.restart_password_page)
        self.btn_for_pass.place(x=45, y=105, width=200)
        self.btn_for_pass.bind('<Motion>',self.cursor_on_restart_password)

        self.window_user.mainloop()