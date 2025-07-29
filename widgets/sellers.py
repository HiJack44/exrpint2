#This is an option menu with sellers

import customtkinter as ctik
from config import config

class SellerList(ctik.CTkOptionMenu):
    def __init__(self, master):
        super().__init__(master)

        self.configure(values=config['Rezervace']['sellers'])
        self.set("Prodejce")

    def get_seller(self):
        return self.get()