from tkinter import *
from MYphonebook import My_PhoneBook

from tkinter import messagebox
import sqlite3
import random

class LoginCommand():

    def Captcha(self):
        self.captcha_stringvar.set('')
        list_char = []
        captcha = ''
        for num in range(1, 6):
            x = random.randint(97 , 122)
            list_char.append(chr(x))
        for char in list_char:
            captcha += char
        self.captcha_stringvar.set(captcha)

    def login_command(self):
        conn = sqlite3.connect("Login.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM loginpage WHERE username = ? AND password = ? ",
                    (self.name_entry.get(), self.pass_entry.get()))
        users = cur.fetchall()
        if self.name_entry.get() == '' or self.pass_entry.get() == '' or self.captcha_entry.get()=='':
            self.login_stringvar.set('')
            messagebox.showinfo('', 'Please Fill the Entries')
            self.login_usename_stringvar.set('')
            self.login_password_stringvar.set('')
            
        elif users != [] and self.captcha_entry.get() == self.captcha_stringvar.get():
            self.captcha_stringvar.set('')
            self.login_stringvar.set('')
            self.login_usename_stringvar.set('')
            self.login_password_stringvar.set('')
            self.root.destroy()
            root = Tk()
            root.title("دفتر تلفن شخصی")
            root.geometry("750x550")
            root.resizable(0, 0)
            app = My_PhoneBook(root)
            app.times()
            app.view_command()
            root.mainloop()
        
        elif users != [] and self.captcha_entry.get() != self.captcha_stringvar.get():
            self.login_stringvar.set('the captcha is failed')
            self.Captcha()
            

        elif users == [] or self.captcha_entry.get() != self.captcha_stringvar.get():
            self.login_stringvar.set('the one of fields is failed')
            self.login_usename_stringvar.set('')
            self.login_password_stringvar.set('')
            self.Captcha()

        cur.close()
        conn.close()