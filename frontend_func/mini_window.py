from tkinter import *
from tkinter import ttk

class MiniWindow:
    """ This class create a window with toplevel from tkinter  """
    def new_window(self , func):
        add = Toplevel()
        add.geometry("500x280")
        add.title("مخاطب جدید را وارد کنید")
        top_frame = Frame(add, height=16)
        top_frame.pack(fill=X)
        bottom_frame = Frame(add, height=40)
        bottom_frame.pack(fill=X)
        for k in range(0, 5):
            if k == 0:
                j = " نام :"
            if k == 1:
                j = " نام خانوادگی :"
            if k == 2:
                j = " جنسیت :"
            if k == 3:
                j = " تلفن :"
            if k == 4:
                j = " آدرس :"
            Label(top_frame, width=10, height=2, font="arial 13 bold", text=j).grid(column=0, row=k)

        for i in range(0, 5):
            if i == 0:
                j = self.FIRSTNAME
                Entry(top_frame, width=40, font="arial 12 bold", textvariable=j) \
                    .grid(column=1, row=i, padx=10, columnspan=5)
            if i == 1:
                j = self.LASTNAME
                Entry(top_frame, width=40, font="arial 12 bold", textvariable=j) \
                    .grid(column=1, row=i, columnspan=5)
            if i == 3:
                j1 = self.PHONE
                j2 = self.MOBILE
                Label(top_frame, width=5, text="ثابت").grid(column=1, row=i)
                Entry(top_frame, width=15, font="arial 12 bold", textvariable=j1) \
                    .grid(column=2, row=i)

                Label(top_frame, width=5, text="موبایل").grid(column=4, row=i)
                Entry(top_frame, width=15, font="arial 12 bold", textvariable=j2) \
                    .grid(column=5, row=i)
            if i == 4:
                j = self.ADDRESS
                Entry(top_frame, width=40, font="arial 12 bold", textvariable=j) \
                    .grid(column=1, row=i, columnspan=5)
            if i == 2:
                pass

        Radiobutton(top_frame, text="آقا", variable=self.GENDER, value="آقا", font=('arial', 14)) \
            .grid(column=1, row=2)
        Radiobutton(top_frame, text="خانوم", variable=self.GENDER, value="خانوم", font=('arial', 14)) \
            .grid(column=2, row=2)

        btn_set = ttk.Button(bottom_frame, text="ذخیره", width=40, command=lambda : func(self))   # this func is into the class (AddMember  or   Update)  --> must be  self 
        btn_set.place(x=150, y=10)

        add.mainloop()