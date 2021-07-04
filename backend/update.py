import sqlite3
from tkinter import * 
from tkinter import messagebox

class Update:
    def update(self):
        self.match_pass.set('')
        conn = sqlite3.connect("Login.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM loginpage")
        conn.commit()
        list_data = []
        my_data = cur.fetchall()
        for data in my_data:
            for i in data:
                list_data.append(i)
        new_pass = self.new_pass_entry.get()
        confirm_pass = self.confirm_pass_entry.get()
        if new_pass == '' or confirm_pass =='':
            self.match_pass.set('')
            self.match_pass.set('Please fill the entries')

        elif new_pass == confirm_pass:
            if new_pass in list_data or confirm_pass in list_data:
                self.match_pass.set('this password is taken')
            else:
                cur.execute("UPDATE loginpage SET password = ? WHERE username = ?",
                            (self.confirm_pass_entry.get(), self.forgot_username.get()))
                self.new_pass_entry.delete(0, END)
                self.confirm_pass_entry.delete(0, END)
                conn.commit()
                conn.close()
                messagebox.showinfo('', 'Password changed successfully')
                self.window_restart_pass.destroy()
                self.window_user.destroy()
                
        elif self.new_pass_entry.get() != self.confirm_pass_entry.get():
            self.match_pass.set('')
            self.match_pass.set('Password not match')