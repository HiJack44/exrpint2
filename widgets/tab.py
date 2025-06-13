#This defines the tabwiew, so we can switch between customers and reservations

import customtkinter as ctik
from widgets import cellframe

class Tab(ctik.CTkTabview):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, **kwargs)

        #self.grid_columnconfigure(0, weight=1)

        #Creating tabs
        self.add("Zákazníci")
        self.add("Rezervace")

        #Placing the cellframe for customer data
        cellfield1 = cellframe.Cellframe(self.tab("Zákazníci"))
        cellfield1.grid(row=0, column=0)

