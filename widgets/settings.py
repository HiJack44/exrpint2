# This is the settings window that will allow the user to customize the app

import customtkinter as ctik
import json, os
from config import config


class Settings(ctik.CTkToplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        path = "../templates/config.json"

        self.geometry("500x500")
        self.title("Nastavení")

        self.nadpis = ctik.CTkLabel(
            self, text="Nastavení", fg_color="transparent", font=("roboto", 20)
        )
        self.nadpis.grid(row=0, column=0, columnspan=2)


def open_settings(parent):
    if parent.settings is None or not parent.settings.winfo_exists():
        parent.settings = Settings(parent)
    else:
        parent.settings.focus_set()
