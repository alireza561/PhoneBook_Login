import sqlite3
from tkinter import messagebox

class Delete:
    """ this class delete one member of database and treeview """

    def delete_data(self):
        id_for_focus = self.tree.focus()
        data_dictionary = self.tree.item(id_for_focus)  
        selectedItem = data_dictionary["values"]   # the values is list  of  self.tree.column
        member_name = selectedItem[1]
        member_lastname = selectedItem[2]



        if not self.tree.selection():
            result = messagebox.showwarning('', 'لطفا یک گزینه را انتخاب کنید', icon="warning")
        else:
            result = messagebox.askquestion('', f'اطمینان دارید؟  {member_name} {member_lastname} آیا از حذف', icon="warning")
            if result == "yes":
                curItem = self.tree.focus()
                contents = self.tree.item(curItem)
                selectedItem = contents["values"]
                self.tree.delete(curItem)
                conn = sqlite3.connect("My_PhoneBook.db")
                cursor = conn.cursor()
                cursor.execute("DELETE FROM member WHERE my_id = %d" % selectedItem[0])
                conn.commit()
                cursor.close()
                conn.close()