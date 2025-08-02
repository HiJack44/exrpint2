# This is the settings window that will allow the user to customize the app

import customtkinter as ctik
import json, os
from config import config
from widgets import settinglabel as sl


class Settings(ctik.CTkToplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        path = os.path.join("templates", "config.json")

        self.geometry("500x500")
        self.title("Nastavení")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header
        self.nadpis = ctik.CTkLabel(
            self, text="Nastavení", fg_color="transparent", font=("roboto", 20)
        )
        self.nadpis.grid(row=0, column=0, columnspan=2)

        # Defining frame with settings options
        self.settings_frame = ctik.CTkScrollableFrame(self)
        self.settings_frame.grid(row=1, column=0, sticky="nsew", columnspan=2)
        self.settings_frame.grid_columnconfigure((0, 1), weight=1)

        # Defining buttons
        self.safe_settings_button = ctik.CTkButton(self, text="Uložit")
        self.safe_settings_button.grid(row=2, column=0, pady=5)

        self.close_settings_button = ctik.CTkButton(self, text="Zavřít")
        self.close_settings_button.grid(row=2, column=1, pady=5)

        testervar = ctik.StringVar(value=config["Format"]["money_sign"])
        self.tester = sl.MenuItem(master=self.settings_frame, text="Tester switch")
        self.tester.grid(row=1, column=0)
        self.test_switch = ctik.CTkSwitch(
            self.settings_frame,
            text="Tester",
            variable=testervar,
            onvalue="1",
            offvalue="0",
        )
        self.test_switch.grid(row=1, column=1)
        # self.test_switch.configure(variable=config['Format']['money_sign'])


def open_settings(parent):
    if parent.settings is None or not parent.settings.winfo_exists():
        parent.settings = Settings(parent)
    else:
        parent.settings.focus_set()
