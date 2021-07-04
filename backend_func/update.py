import sqlite3
from tkinter import messagebox
from .viewcontacts import ViewContacts

class Update:
    """ This class edits the member you select of treeview"""
    def update_data(self):
        id_for_focus = self.tree.focus()
        data_dictionary = self.tree.item(id_for_focus)  
        selectedItem = data_dictionary["values"]   # the values is list  of  self.tree.column
        member_id = selectedItem[0]   # the 0th index of list from self.tree.column  is  id  in database

        try:
            if self.GENDER.get() == "":
                messagebox.showwarning('', 'لطفا جنسیت را تعیین کنید', icon="warning")
            else:
                self.tree.delete(*self.tree.get_children())
                conn = sqlite3.connect("My_PhoneBook.db")
                cursor = conn.cursor()
                cursor.execute(
                    f"""
                    UPDATE member SET firstname='{str(self.FIRSTNAME.get())}', lastname='{str(self.LASTNAME.get())}',
                    gender='{str(self.GENDER.get())}', phone='{ int(self.PHONE.get())}', mobile={int(self.MOBILE.get())},
                    address='{str(self.ADDRESS.get())}' WHERE my_id='{int(member_id)}'
                    """
                    )
                conn.commit()
                cursor.execute("SELECT * FROM member")
                fetch = cursor.fetchall()
                for data in fetch:
                    self.tree.insert('', 'end', values=data)
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