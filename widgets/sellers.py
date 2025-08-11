# This is an option menu with sellers

import customtkinter as ctik
from config import config
from config import save_config as sc


class SellerList(ctik.CTkOptionMenu):
    def __init__(self, master):
        super().__init__(master)

        self.data = config
        self.seller_data = self.data['Rezervace']['sellers']

        self.configure(values=self.seller_data)
        self.set("Prodejce")

    def get_seller(self):
        return self.get()

    def add_seller(self, name):
        self.seller_data = self.seller_data.append(name)
        sc(self.data)

    def remove_seller(self):
        ...
