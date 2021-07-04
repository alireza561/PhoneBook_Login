import sqlite3
from tkinter import *
from tkinter import messagebox
class SignUpCommand:
    def sign_up_command(self):
        self.sing_up_eror.set('')
        conn = sqlite3.connect('Login.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM loginpage")
        conn.commit()
        my_data = cur.fetchall()
        list_data = []
        username = self.usereg_entry.get()
        password = self.passreg_entry.get()
        if self.usereg_entry.get() == '' and self.passreg_entry.get() == '':
            self.sing_up_eror.set('Please fill the entries')
        if self.usereg_entry.get() != '' and self.passreg_entry.get() != '':
            for data in my_data:
                for i in data:
                    list_data.append(i)
            if username in list_data or password in list_data:
                self.sing_up_eror.set('username or password is taken')
            else:
                self.insert()
                self.usereg_entry.delete(0, END)
                self.passreg_entry.delete(0, END)
                self.window3.destroy()
                messagebox.showinfo('', 'user added')
