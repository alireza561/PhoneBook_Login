from tkinter import *
from tkinter import ttk
from .topframe import TopFrame

class BottomFrame:
    """ this class create a frame in the bottom of master  And  master is Tk()  from tkinter"""
    def __init__(self, master):
        self.master = master
        self.bottom_frame = Frame(master, bg="white", height=72)
        self.bottom_frame.pack(fill=X)

        self.btn_search = ttk.Button(self.bottom_frame,
                                     text="جستجو", width=12, command=self.search_command)
        self.btn_search.place(x=660, y=5)

        self.btn_view = ttk.Button(self.bottom_frame,
                                   text="نمایش همه", width=12, command=self.view_command)
        self.btn_view.place(x=660, y=40)

        self.label_search = ttk.Label(self.bottom_frame,
                                      text=" کدام گزینه", font=('', 12), foreground='black', background='white')
        self.label_search.place(x=590, y=5)

        self.combo_string = StringVar()
        self.combobox = ttk.Combobox(self.bottom_frame,
                                         width=10, font=("", 10, "bold"), textvariable=self.combo_string,
                                         state="readonly")
        self.combobox["value"] = ("firstname", "lastname", "phone")
        self.combobox.place(x=500, y=5)
        

        self.text_search = StringVar()
        self.entry_search = ttk.Entry(self.bottom_frame, font=("times new roman", 12), textvariable=self.text_search)
        self.entry_search.place(x=320, y=5)