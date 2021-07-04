class BindsMethod:
    def cursor_on_sign_up(self, event):
        self.btn_signup.config(font=('comic sans ms', 13, 'bold'))
        self.btn_signup.place(x=165, y=323)
        self.btn_log.config(background='#0488c9') #chon beine btnlog va btnforgot fasele nist pas mos roye mainframe nemire
        self.btn_forgotpass.config(foreground='#733603')  # pas bayad inja begim btnlog va forgot be halate aval bargarde

    def cursor_on_main_frame(self, event):
        self.btn_signup.config(font=('comic sans ms', 11))
        self.btn_signup.place(x=165, y=326)
        self.btn_log.config(background='#0488c9')
        self.btn_forgotpass.config(foreground='#733603')

    def cursor_on_btn_log_in(self, event):
        self.btn_log.config(background='#00abff')
        self.btn_forgotpass.config(foreground='#733603')

    def cursor_on_btn_forgot_pass(self,event):
        self.btn_forgotpass.config(foreground='#0000b3')
        self.btn_signup.config(font=('comic sans ms', 11))
        self.btn_signup.place(x=165, y=326)
        self.btn_log.config(background='#0488c9')

    def cursor_on_restart_password(self, event):
        self.btn_for_pass.config(background="fuchsia")
    
    def cursor_on_bottomframe_restartpass(self, event):
        self.btn_new_pass.config(background='#fc0390')

    def cursor_on_mainframe_forgot(self, event):
        self.btn_for_pass.config(background='#fc0390')

    def cursor_on_btn_new_pass(self, event):
        self.btn_new_pass.config(background="fuchsia")

    def cursor_on_mainframe_restart(self, event):
        self.btn_new_pass.config(background='#fc0390')

    def cursor_on_btn_register(self, event):
        self.btn_register.config(background='#5ad219')

    def cursor_on_bottom_frame_registration(self, event):
        self.btn_register.config(background='#00ff0d')