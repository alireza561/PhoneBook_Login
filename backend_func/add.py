import sqlite3
from tkinter import messagebox
from .viewcontacts import ViewContacts
class AddMember:
    """ this class add one member to database and treeview """
    def add_member(self):
        try:
            if self.FIRSTNAME.get() == "" or self.LASTNAME.get() == "" or self.GENDER.get() == "" or \
                    self.PHONE.get() == "" or self.MOBILE.get() == "" or self.ADDRESS.get() == "":
                messagebox.showwarning('', 'لطفا تمام فیلد ها را کامل کنید', icon="warning")

            else:
                self.tree.delete(*self.tree.get_children())
                conn = sqlite3.connect("My_PhoneBook.db")
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO member VALUES(NULL , ?, ?, ?, ?, ?, ?)",
                    (
                        str(self.FIRSTNAME.get()), str(self.LASTNAME.get()), str(self.GENDER.get()),
                    int(self.PHONE.get()), int(self.MOBILE.get()), str(self.ADDRESS.get()))
                )
                    
                conn.commit()
                cursor.execute("SELECT * FROM member")
                fetch = cursor.fetchall()
                for data in fetch:
                    self.tree.insert('' , 'end', values=data)
                cursor.close()
                conn.close()
                self.FIRSTNAME.set("")
                self.LASTNAME.set("")
                self.GENDER.set("")
                self.PHONE.set("")
                self.MOBILE.set("")
                self.ADDRESS.set("")

        except Exception :
            ViewContacts.view_command(self)
            messagebox.showwarning('', 'تلفن و موبایل باید عدد باشند', icon="warning")