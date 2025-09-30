# This module contains the Help window for the user
# It is a TopLevel window with simple menu describing each
# function of the app

import customtkinter as ctik
from pathlib import Path

class HelpWindow(ctik.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry("700x700")
        self.title("Nápověda")
        self.attributes("-topmost", True)

    data_path = Path().joinpath("templates", "help.py")
    print(data_path)



    def close_help(self):
        self.destroy()



def open_help(parent):
    if parent.help_window is None or not parent.help_window.winfo_exists():
        parent.help_window = HelpWindow(parent)
        parent.help_window.focus_set()
    else:
        parent.help_window.focus_set()