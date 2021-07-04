import sqlite3
from tkinter import *
from tkinter import messagebox

class Search:
    """ This class will find the member you want  """
    def search_command(self):
        try:

            conn = sqlite3.connect("My_PhoneBook.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM member WHERE " +
                           self.combo_string.get() + " LIKE '%" + self.text_search.get() + "%'")  # in yani az avalin
            # harf ta akharin harfe text_search ro begir va search kon
            rows = cursor.fetchall()  # inja cursor migarde va oon chizi ke khate bala goftim ejra ya execute kone ro
            # peida mikone

            self.tree.delete(*self.tree.get_children())
            if self.entry_search.get() == "":
                messagebox.showwarning('', "گزینه ها خالی است")

            elif rows:  # yani age row dashtim yani age dar database yek satr az data ha dashtim az name ,lastname,...
                for row in rows:
                    self.tree.insert("", END, values=row)

            else:
                messagebox.showwarning('', "نتیجه ای یافت نشد")
            cursor.close()
            conn.close()
            self.text_search.set('')
            self.combo_string.set('')
        except:
            messagebox.showwarning('', "لطفا یک گزینه انتخاب کنید")