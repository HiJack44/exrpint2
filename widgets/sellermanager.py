#This is a top-level window with options to add or remove seller

import customtkinter as ctik
from config import config
from config import save_config as sc

class SellerManager(ctik.CTkToplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.geometry("300x500")
        self.title("Přidat nebo odebrat prodejce")

        self.seller_manager_label = ctik.CTkLabel(self, text="Přidat nebo odebrat prodejce", fg_color='transparent')
        self.seller_manager_label.grid(row=0, column=0, columnspan=2)

        """Input seller section to add new seller to the list"""
        # Frame to ecapsulate input seller section
        self.input_seller_frame = ctik.CTkFrame(self, border_width=2, border_color='black', fg_color='transparent')
        self.input_seller_frame.grid(row=1, column=0)

        self.input_seller_label = ctik.CTkLabel(self.input_seller_frame, text="Nový prodejce", fg_color='transparent')
        self.input_seller_label.grid(row=0, column=0, padx=5, pady=5)

        self.input_seller_field = ctik.CTkEntry(self.input_seller_frame)
        self.input_seller_field.grid(row=1, column=0, padx=5, pady=5)

        self.input_seller_add_button = ctik.CTkButton(self.input_seller_frame, text="Přidat")
        self.input_seller_add_button.grid(row=2, column=0, padx=5, pady=5)

        """Remove seller section to remove sellers from the list"""
        self.remove_seller_frame = ctik.CTkFrame(self, border_width=2, border_color="black", fg_color='transparent')
        self.remove_seller_frame.grid(row=2, column=0)

        """Button section"""
        self.close_button = ctik.CTkButton(self, text="Zavřít", command=self.close_seller_manager)
        self.close_button.grid(row=3, column=0, padx=5, pady=5)


    def close_seller_manager(self):
        self.destroy()
    def save_seller_manager(self, lister):
        ...

def open_seller_manager(parent):
    if parent.sellermanager is None or not parent.sellermanager.winfo_exists():
        parent.sellermanager = SellerManager(parent)
    else:
        parent.sellermanager.focus()