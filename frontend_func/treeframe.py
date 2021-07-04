from tkinter import *
from tkinter import ttk
from .topframe import TopFrame

class TreeFrame(TopFrame):
    """ this class create a frame for  treeview into the master  And  master is Tk()  from tkinter"""
    def __init__(self , master) :
        super().__init__(master)
        self.treeFrame = Frame(master, width=650, height=450, bg="blue")
        self.treeFrame.pack(side=TOP)

        self.scrollbar_x = Scrollbar(self.treeFrame, orient=HORIZONTAL)
        self.scrollbar_y = Scrollbar(self.treeFrame, orient=VERTICAL)
        self.tree = ttk.Treeview(self.treeFrame,
                                 columns=("شناسه", "نام", "نام خانوادگی", "جنسیت", "تلفن", "موبایل", "آدرس"),
                                 height=20, selectmode="extended", yscrollcommand=self.scrollbar_y.set,
                                 xscrollcommand=self.scrollbar_x.set)
        

        self.tree.heading("شناسه", text="شناسه")
        self.tree.heading("نام", text="نام")
        self.tree.heading("نام خانوادگی", text="نام خانوادگی")
        self.tree.heading("جنسیت", text="جنسیت")
        self.tree.heading("تلفن", text="تلفن")
        self.tree.heading("موبایل", text="موبایل")
        self.tree.heading("آدرس", text="آدرس")

        self.tree.column("نام", anchor="center")
        self.tree.column("نام خانوادگی", anchor="center")
        self.tree.column("جنسیت", anchor="center")
        self.tree.column("تلفن", anchor="center")
        self.tree.column("موبایل", anchor="center")
        self.tree.column("آدرس", anchor="center")

        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=40)
        self.tree.column('#2', stretch=NO, minwidth=0, width=80)
        self.tree.column('#3', stretch=NO, minwidth=0, width=100)
        self.tree.column('#4', stretch=NO, minwidth=0, width=50)
        self.tree.column('#5', stretch=NO, minwidth=0, width=120)
        self.tree.column('#6', stretch=NO, minwidth=0, width=120)
        self.tree.column('#7', stretch=NO, minwidth=0, width=180)

        self.scrollbar_x.config(command=self.tree.xview)
        self.scrollbar_x.pack(side=BOTTOM, fill=X)
        self.scrollbar_y.config(command=self.tree.yview)
        self.scrollbar_y.pack(side=RIGHT, fill=Y)

        self.tree.pack(side=TOP)