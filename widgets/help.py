# This module contains the Help window for the user
# It is a TopLevel window with simple menu describing each
# function of the app
import json

import customtkinter as ctik
from pathlib import Path

class HelpWindow(ctik.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry("700x700")
        self.title("Nápověda")
        self.attributes("-topmost", True)
        self.grid_columnconfigure(1, weight=1)

        #Menu Frame
        self.menu_frame = ctik.CTkFrame(self)
        self.menu_frame.grid(row=0, column=0)
        self.menu_frame.grid_columnconfigure(0, weight=1)

        # Topic frame
        self.topic_frame = ctik.CTkFrame(self)
        self.topic_frame.grid(row=0, column=1)
        self.topic_frame.grid_columnconfigure(0, weight=1)

        # Fetching data from help.json
        data_path = Path().joinpath("templates", "help.json")
        print(data_path)
        with open(data_path, "r", encoding="utf-8") as helper:
            self.helper_data = json.load(helper)

        #Placing the default header
        self.help_header = ctik.CTkLabel(self.topic_frame, text=next(iter(self.helper_data)), font=("Roboto", 40))
        self.help_header.grid(row=0, column=0)
        # Placing first label. Default is About page
        self.help_page = ctik.CTkLabel(self.topic_frame, text=self.helper_data["O aplikaci"]["text"])
        self.help_page.grid(row=1, column=0)

        # Defining menu buttons
        for i, key in enumerate(self.helper_data):
            print(key)
            print(self.helper_data[key]["text"])
            self.topic_button = ctik.CTkButton(self.menu_frame,
                                          text=key,
                                          command=lambda master=self, item=key: load_topic(master,item))
            self.topic_button.grid(row=i, column=0, sticky="w")

def load_topic(master,topic):
    """
    :param topic: The text value from the topic in helper
    :return: text value
    """
    master.help_header.configure(text=topic)
    master.help_page.configure(text=master.helper_data[topic]["text"])




def close_help(master):
    master.destroy()



def open_help(parent):
    if parent.help_window is None or not parent.help_window.winfo_exists():
        parent.help_window = HelpWindow(parent)
        parent.help_window.focus_set()
    else:
        parent.help_window.focus_set()