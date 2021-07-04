from tkinter import *
import sqlite3

from frontend.login import Login
from frontend.forgot_page import Forgot
from frontend.restart_password_page import RestartPasswordPage
from frontend.signup_page import SignUp

from backend.methods_cursor_bind import BindsMethod
from backend.login import LoginCommand
from backend.signup import SignUpCommand
from backend.insert import Insert
from backend.update import Update

class LoginPage(Login, Forgot, RestartPasswordPage, SignUp, BindsMethod, LoginCommand,
 SignUpCommand, Insert, Update):

    def __init__(self):
        Login.__init__(self)
        self.match_pass = StringVar()
        self.forgot_label_username_stringvar = StringVar()
        self.sing_up_eror = StringVar()
        self.forgot_username = StringVar()
    
        self.root.mainloop()

        self.conn = sqlite3.connect('Login.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS loginpage (
            username TEXT(70) ,
            password TEXT(70)
        ) """)

def main():
    LoginPage()

if __name__ == '__main__':
    main()