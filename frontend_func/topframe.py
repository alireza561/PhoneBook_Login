from tkinter import *
from tkinter import ttk
import time

class TopFrame:
    """ this class create a frame in the top of master  And  master is Tk()  from tkinter"""
    def __init__(self , master) :
        self.master = master
        self.top = Frame(master, bg="white", height=30)
        self.top.pack(fill=X)

        self.clock = Label(self.top, font=("times", 12, "bold"), bg="white", width=15)
        self.clock.place(x=480, y=6)

        self.Image = PhotoImage(file="./image/pbb.png")
        self.label_image = Label(self.top, text="دفتر تلفن ", bg="white", fg="gray", font="arial 18 bold",
                            image=self.Image)
        self.label_image.config(compound=RIGHT)
        self.label_image.pack(side=LEFT)

        self.btn_add = ttk.Button(self.top, text="+", width=5, command=self.add_window)
        self.btn_add.place(x=120, y=5)

        self.btn_delete = ttk.Button(self.top, text="حذف", width=6, command=self.delete_data)
        self.btn_delete.place(x=165, y=5)

        self.btn_update = ttk.Button(self.top, text="ویرایش", width=8, command=self.update_window)
        self.btn_update.place(x=220, y=5)

    def times(self):
        my_time = time.strftime('%I:%M:%S', time.localtime())
        self.clock.config(text=my_time, font='times 12')
        self.clock.after(100, self.times)