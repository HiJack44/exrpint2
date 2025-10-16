# This module contains the Help window for the user
# It is a TopLevel window with simple menu describing each
# function of the app
import json

import customtkinter as ctik
from pathlib import Path
from PIL import Image

class HelpWindow(ctik.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry("900x700")
        self.title("Nápověda")
        self.attributes("-topmost", True)
        self.grid_columnconfigure(1, weight=1)

        #Menu Frame
        self.menu_frame = ctik.CTkFrame(self)
        self.menu_frame.grid(row=0, column=0)
        self.menu_frame.grid_columnconfigure(0, weight=1)

        # Topic frame
        self.topic_frame = ctik.CTkScrollableFrame(self, width=750, height=690)
        self.topic_frame.grid(row=0, column=1)
        self.topic_frame.grid_columnconfigure(0, weight=1)
        self.topic_frame.grid_rowconfigure((0,1,2), weight=1)

        # Fetching data from help.json
        data_path = Path().joinpath("templates", "help.json")
        print(data_path)
        with open(data_path, "r", encoding="utf-8") as helper:
            self.helper_data = json.load(helper)

        #Placing the default header
        self.help_header = ctik.CTkLabel(self.topic_frame, text=next(iter(self.helper_data)), font=("Roboto", 40))
        self.help_header.grid(row=0, column=0)

        # Placing first label. Default is About page
        self.help_page = ctik.CTkLabel(self.topic_frame,
                                       text=self.helper_data["O aplikaci"]["text"],
                                       wraplength=640, justify='left'
                                       )
        self.help_page.grid(row=1, column=0)

        # Placing first image
        home_path = Path().resolve()
        img_folder_path = home_path/"img"
        self.help_image = ctik.CTkImage(dark_image=Image.open(img_folder_path/"about.jpg"),
                                        size=(640,480))
        self.help_image_label = ctik.CTkLabel(self.topic_frame,text="", image=self.help_image)
        self.help_image_label.grid(row=2, column=0)



        # Defining menu buttons
        for i, key in enumerate(self.helper_data):
            #print(key)
            #print(self.helper_data[key]["text"])
            self.topic_button = ctik.CTkButton(self.menu_frame,
                                          text=key,
                                          command=lambda master=self, item=key, img_folder=img_folder_path: load_topic(master,item, img_folder))
            self.topic_button.grid(row=i, column=0, sticky="w")

# This function switches the topic
def load_topic(master,topic, img_folder):
    """
    :param topic: The text value from the topic in helper
    :return: change of text of the topic header and text
    """
    master.help_header.configure(text=topic)
    master.help_page.configure(text=master.helper_data[topic]["text"])
    new_pic = img_folder/master.helper_data[topic]["pic"]
    master.help_image.configure(dark_image=Image.open(new_pic))




def close_help(master):
    master.destroy()



def open_help(parent):
    if parent.help_window is None or not parent.help_window.winfo_exists():
        parent.help_window = HelpWindow(parent)
        parent.help_window.focus_set()
    else:
        parent.help_window.focus_set()