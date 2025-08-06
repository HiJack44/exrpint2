# This is the settings window that will allow the user to customize the app

import customtkinter as ctik
import json, os
from config import config, save_config
from config import save_config as sc
from widgets import settinglabel as sl


class Settings(ctik.CTkToplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # path = os.path.join("templates", "config.json")

        self.geometry("500x500")
        self.title("Nastavení")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(1, weight=1)

        data = config

        # Defining frame with settings options
        self.settings_frame = ctik.CTkScrollableFrame(self)
        self.settings_frame.grid(row=1, column=0, sticky="nsew", columnspan=2)
        self.settings_frame.grid_columnconfigure((0, 1), weight=1)

        # Defining frames for each part of settings
        self.general_settings_frame = ctik.CTkFrame(
            self.settings_frame, border_width=2, border_color="black"
        )
        self.general_settings_frame.grid(row=0, column=0, columnspan=3, pady=5)
        self.general_settings_label = ctik.CTkLabel(
            self.general_settings_frame, text="Obecné", fg_color="transparent"
        )
        self.general_settings_label.grid(
            row=0, column=0, columnspan=3, padx=3, pady=(5, 0), sticky="ew"
        )

        self.cus_settings_frame = ctik.CTkFrame(
            self.settings_frame, border_width=2, border_color="black"
        )
        self.cus_settings_frame.grid(row=1, column=0, columnspan=3, pady=5)
        self.cus_settings_label = ctik.CTkLabel(
            self.cus_settings_frame, text="Zákazníci", fg_color="transparent"
        )
        self.cus_settings_label.grid(
            row=0, column=0, padx=3, pady=(5, 0), columnspan=3, sticky="ew"
        )

        self.res_settings_frame = ctik.CTkFrame(
            self.settings_frame, border_width=2, border_color="black"
        )
        self.res_settings_frame.grid(row=2, column=0, columnspan=3, pady=5)
        self.res_settings_label = ctik.CTkLabel(
            self.res_settings_frame, text="Rezervace", fg_color="transparent"
        )
        self.res_settings_label.grid(
            row=0, column=0, columnspan=3, padx=3, pady=(5, 0), sticky="ew"
        )

        # Header
        self.nadpis = ctik.CTkLabel(
            self, text="Nastavení", fg_color="transparent", font=("roboto", 20)
        )
        self.nadpis.grid(row=0, column=0, columnspan=2)

        # Defining buttons
        # Save button, that wil trigger function to rewrite config.json
        self.safe_settings_button = ctik.CTkButton(
            self, text="Uložit", command=lambda data=data: self.save_settings(data)
        )
        self.safe_settings_button.grid(row=2, column=0, pady=5)

        # Close button will ignore changes and close settings window
        self.close_settings_button = ctik.CTkButton(
            self, text="Zavřít", command=self.close_settings
        )
        self.close_settings_button.grid(row=2, column=1, pady=5)

        """GENERAL SETTINGS SECTION"""
        """This section is for general settings"""

        """"CUSTOMERS SETTING SECTION"""
        """"This section is for setup of the Customers window"""
        # Currency switch
        money_sign_switch_var = ctik.StringVar(value=config["Format"]["money_sign"])
        self.money_sign_switch_label = sl.MenuItem(
            master=self.cus_settings_frame, text="Měna"
        )
        self.money_sign_switch_label.grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
        )
        self.money_sign_switch = ctik.CTkSwitch(
            self.cus_settings_frame,
            text="",
            variable=money_sign_switch_var,
            onvalue="1",
            offvalue="0",
        )
        self.money_sign_switch.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Currency signs list
        money_sign_list_var = ctik.StringVar(
            value=config["Format"]["active_money_sign"]
        )
        self.money_sign_list_label = sl.MenuItem(
            master=self.cus_settings_frame, text="Znak měny"
        )
        self.money_sign_list_label.grid(row=2, column=0, padx=5, pady=5)
        self.money_sign_list = ctik.CTkOptionMenu(
            self.cus_settings_frame,
            width=60,
            variable=money_sign_list_var,
            values=config["Format"]["money_sign_list"],
        )
        self.money_sign_list.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Date adder
        date_adder_var = ctik.StringVar(value=config["Format"]["date"])
        self.date_adder_label = ctik.CTkLabel(self.cus_settings_frame, text="Datum")
        self.date_adder_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.date_adder_switch = ctik.CTkSwitch(
            self.cus_settings_frame,
            text="",
            variable=date_adder_var,
            onvalue="1",
            offvalue="0",
        )
        self.date_adder_switch.grid(row=4, column=1, padx=5, pady=5)

        """"RESERVATION SETTINGS SECTION"""
        """This section is for reservation settings"""

    def close_settings(self):
        self.destroy()

    def save_settings(self, data):
        data["Format"]["money_sign"] = self.money_sign_switch.get()
        data["Format"]["active_money_sign"] = self.money_sign_list.get()
        data["Format"]["date"] = self.date_adder_switch.get()
        sc(data)
        self.close_settings()


def open_settings(parent):
    if parent.settings is None or not parent.settings.winfo_exists():
        parent.settings = Settings(parent)
    else:
        parent.settings.focus_set()
