# This is a top-level window with options to add or remove seller
from sys import maxsize

import customtkinter as ctik
import re
from config import config
from config import save_config as sc
from widgets import sellers
from widgets import alertwindow as alwi


class SellerManager(ctik.CTkToplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.geometry("200x330")
        self.title("Přidat nebo odebrat prodejce")
        self.maxsize(width=220, height=340)

        self.attributes("-topmost", True)

        data = config

        self.seller_manager_label = ctik.CTkLabel(
            self, text="Přidat nebo odebrat prodejce", fg_color="transparent"
        )
        self.seller_manager_label.grid(row=0, column=0, sticky='ew')

        """Input seller section to add new seller to the list"""
        # Frame to encapsulate input seller section
        self.input_seller_frame = ctik.CTkFrame(
            self, border_width=2, border_color="black", fg_color="transparent"
        )
        self.input_seller_frame.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

        self.input_seller_frame.grid_columnconfigure(0, weight=1)

        self.input_seller_label = ctik.CTkLabel(
            self.input_seller_frame, text="Nový prodejce", fg_color="transparent"
        )
        self.input_seller_label.grid(row=0, column=0, padx=5, pady=5)

        self.input_seller_field = ctik.CTkEntry(self.input_seller_frame)
        self.input_seller_field.grid(row=1, column=0, padx=5, pady=5)

        self.input_seller_add_button = ctik.CTkButton(
            self.input_seller_frame,
            text="Přidat",
            command=lambda alldata=data, master=parent: add_seller(alldata, master),
        )
        self.input_seller_add_button.grid(row=2, column=0, padx=5, pady=(5,10))

        # This function adds new seller to the list
        def add_seller(alldata, master):
            new_name = self.input_seller_field.get()
            new_name = new_name.strip()
            if not re.match("^[a-zA-Z]+$", new_name) or len(new_name) > 8:
                decline = alwi.open_alert(
                    master,
                    "Špatný formát jména",
                    "Zadané jméno prodejce je ve špatném formátu.\n "
                    "Povolené znaky jsou pouze a-z, A-Z a maximální délka je 8 znaků",
                )
            else:
                self.input_seller_field.delete("0", "end")
                alldata["Rezervace"]["sellers"].append(new_name)
                sc(alldata)
                confirm = alwi.open_alert(
                    master,
                    "Přidán nový prodejce",
                    f"Nový prodejce přidán\n{new_name}\nZměna se projeví až po restartu aplikace",
                )


        """Remove seller section to remove sellers from the list"""
        self.remove_seller_frame = ctik.CTkFrame(
            self, border_width=2, border_color="black", fg_color="transparent"
        )
        self.remove_seller_frame.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

        self.remove_seller_frame.grid_columnconfigure(0, weight=1)

        self.remove_seller_label = ctik.CTkLabel(
            self.remove_seller_frame, text="Odstranit prodejce", fg_color="transparent"
        )
        self.remove_seller_label.grid(row=0, column=0, padx=5, pady=5)

        self.remove_seller_list = sellers.SellerList(self.remove_seller_frame)
        # self.remove_seller_list.sort()
        self.remove_seller_list.grid(row=1, column=0, pady=5, padx=5)

        self.remove_seller_button = ctik.CTkButton(
            self.remove_seller_frame,
            text="Odstranit",
            command=lambda alldata=data, master=parent: remove_seller(alldata, master),
        )
        self.remove_seller_button.grid(row=2, column=0, padx=5, pady=(5,10))

        def remove_seller(alldata, master):
            seller_to_del = self.remove_seller_list.get()
            alldata["Rezervace"]["sellers"].remove(seller_to_del)
            sc(alldata)
            msg = f"Prodejce {seller_to_del} byl odstraněn.\nZměna se projeví po restartu aplikace"
            confirm = alwi.open_alert(master, "Prodejce odstraněn", msg)

        """Button section"""
        self.close_button = ctik.CTkButton(
            self, text="Zavřít", command=self.close_seller_manager
        )
        self.close_button.grid(row=3, column=0, padx=5, pady=5)


    def close_seller_manager(self):
        self.destroy()

    def save_seller_manager(self, lister): ...


def open_seller_manager(parent):
    if parent.sellermanager is None or not parent.sellermanager.winfo_exists():
        parent.sellermanager = SellerManager(parent)
        parent.sellermanager.focus()
    else:
        parent.sellermanager.focus()
