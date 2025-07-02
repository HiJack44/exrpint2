# This defines the tabwiew, so we can switch between customers and reservations

import customtkinter as ctik
from widgets import cellframe


class Tab(ctik.CTkTabview):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        # Creating tabs
        self.add("Zákazníci")
        self.add("Rezervace")

        # Placing the cellframe for reservation data
        self.reserv1 = cellframe.Cellframe(
            self.tab("Rezervace"),
            row_count=10,
            col_count=2,
            cw=150,
            ch=1,
            width=500,
            height=400,
        )
        self.reserv1.grid(row=0, column=0, sticky="nsew", columnspan=3)

        # Placing the cellframe for customer data
        self.cellfield1 = cellframe.Cellframe(
            self.tab("Zákazníci"),
            row_count=15,
            col_count=8,
            cw=100,
            ch=1,
            width=900,
            height=600,
        )
        self.cellfield1.grid(row=0, column=0, sticky="nsew")
