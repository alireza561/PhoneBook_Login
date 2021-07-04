from tkinter import *
import sqlite3
from tkinter import messagebox
from frontend_func.treeframe import TreeFrame
from frontend_func.bottomframe import BottomFrame
from frontend_func.mini_window import MiniWindow
from backend_func.viewcontacts import ViewContacts
from backend_func.search import Search
from backend_func.add import AddMember
from backend_func.delete import Delete
from backend_func.update import Update

class My_PhoneBook(TreeFrame , BottomFrame , ViewContacts , Search , AddMember , Delete , Update , MiniWindow):
    def __init__(self, master):
        TreeFrame.__init__(self , master)
        BottomFrame.__init__(self , master)

        self.FIRSTNAME = StringVar()
        self.LASTNAME = StringVar()
        self.GENDER = StringVar()
        self.PHONE = StringVar()
        self.MOBILE = StringVar()
        self.ADDRESS = StringVar()

        self.conn = sqlite3.connect("My_PhoneBook.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS member(
            my_id INTEGER PRIMARY KEY ,
            firstname TEXT,
            lastname TEXT ,
            gender TEXT ,
            phone INTEGER ,
            mobile INTEGER ,
            address TEXT
        )""")
        self.conn.commit()

    def add_window(self):
        MiniWindow.new_window(self , AddMember.add_member)
       
    def update_window(self):
        if not self.tree.selection():
            messagebox.showwarning('', 'لطفا یک مورد را انتخاب کنید', icon="warning")
        else:
            curItem = self.tree.focus()
            contents = self.tree.item(curItem)
            selectedItem = contents["values"]
            member_id = selectedItem[0]
            self.FIRSTNAME.set(selectedItem[1])
            self.LASTNAME.set(selectedItem[2])
            self.PHONE.set(selectedItem[4])
            self.MOBILE.set(selectedItem[5])
            self.ADDRESS.set(selectedItem[6])

            MiniWindow.new_window(self , Update.update_data)