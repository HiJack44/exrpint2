#This defines the tabwiew, so we can switch between customers and reservations

import customtkinter as ctik
from widgets import cellframe

class Tab(ctik.CTkTabview):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        #Creating tabs
        self.add("Zákazníci")
        self.add("Rezervace")

        #Placing the cellframe for customer data
        self.cellfield1 = cellframe.Cellframe(self.tab("Zákazníci"), row_count=10, col_count=8, cw=40, ch=1, width=250)
        self.cellfield1.grid(row=0, column=0)

        #Placing the cellframe for reservation data
        reserv1 = cellframe.Cellframe(self.tab("Rezervace"), row_count=6, col_count=1, cw=200, ch=1, width=200)
        reserv1.grid(row=0, column=0)



