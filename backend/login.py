from frontend.login import Login
from tkinter import *
from MYphonebook import My_PhoneBook

from tkinter import messagebox
import sqlite3
class LoginCommand:
    def login_command(self):
        conn = sqlite3.connect("Login.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM loginpage WHERE username = ? AND password = ? ",
                    (self.name_entry.get(), self.pass_entry.get()))
        users = cur.fetchall()
        if self.name_entry.get() == '' or self.pass_entry.get() == '':
            self.login_stringvar.set('')
            messagebox.showinfo('', 'Please Fill the Entries')
            self.login_usename_stringvar.set('')
            self.login_password_stringvar.set('')
            
        elif users != []:
            self.login_stringvar.set('')
            self.login_usename_stringvar.set('')
            self.login_password_stringvar.set('')
            self.root.destroy()
            # messagebox.showinfo('', 'user logged')
            root = Tk()
            root.title("دفتر تلفن شخصی")
            root.geometry("750x550")
            root.resizable(0, 0)
            app = My_PhoneBook(root)
            app.times()
            app.view_command()
            root.mainloop()
            

        elif users == []:
            self.login_stringvar.set('username or password is failed')
            self.login_usename_stringvar.set('')
            self.login_password_stringvar.set('')

        cur.close()
        conn.close()