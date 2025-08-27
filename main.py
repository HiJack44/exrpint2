import json

import customtkinter as ctik
import requests, zipfile, os, io
from widgets import stickerframe, tab, sellers, settings
from utils import events as ev
from utils import formatter as f
from utils import print as p
from config import config

APP_VERSION = "1.0.0"
API_SOURCE = 'https://api.github.com/repos/HiJack44/exrpint2/releases'

ctik.set_default_color_theme("templates/theme_dark.json")
ctik.set_appearance_mode("dark")

# Main function of the program
class App(ctik.CTk):
    def __init__(self):
        super().__init__()

        # Defining the window
        self.geometry("1250x700")
        self.minsize(1250, 700)
        self.title("Exprint 2")


        # Placing top bar
        self.top_bar = ctik.CTkFrame(self, height=20, corner_radius=0)
        self.top_bar.grid(row=0, column=0, columnspan=2, sticky="nswe")
        self.top_bar.grid_columnconfigure(1, weight=1)

        # Placing setup button and Nonefying settings window
        self.settings = None
        self.settings_button = ctik.CTkButton(
            self.top_bar,
            text="Nastavení",
            fg_color="transparent",
            command=lambda parent=self: settings.open_settings(parent)
        )
        self.settings_button.grid(row=0, column=0, padx=5, pady=5)

        #Placing reload button
        self.reload_button = ctik.CTkButton(self.top_bar, text = "Reload", fg_color='transparent', command=self.restart)
        self.reload_button.grid(row=0, column=1, padx=5, pady=5, sticky='e')

        # Placing the tabview with cellframes
        self.tabview = tab.Tab(self)
        self.tabview.grid(row=1, column=0, padx=(5, 0), sticky="nsw")

        # Placing stickerframe which will be displaying formated stickers
        self.stickerframe = stickerframe.Stickerframe(self, width=280, height=600)
        self.stickerframe.grid(row=1, column=1, padx=5, pady=(20,0), sticky="nsew")

        # Placing frame for customers buttons
        self.cus_button_frame = ctik.CTkFrame(
            self.tabview.cellfield1, fg_color='transparent'
        )
        self.cus_button_frame.grid(row=0, column=0, sticky="we", columnspan=10)
        self.cus_button_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # Placing frame for buttons for reservations
        self.res_button_frame = ctik.CTkFrame(
            self.tabview.reserv1, fg_color="transparent"
        )
        self.res_button_frame.grid(row=0, column=0, columnspan=2, sticky="we")
        self.res_button_frame.grid_columnconfigure((0, 1), weight=1)

        # Placing buttons
        # Format Button - customers
        self.format_button_zak = ctik.CTkButton(
            self.cus_button_frame,
            text="Format",
            command=lambda master=self.tabview.cellfield1, submaster=self.stickerframe: ev.format_handler(
                master, submaster
            ),
        )
        self.format_button_zak.grid(
            row=0,
            column=0,
            padx=config["Button_bar"]["padx"],
            pady=config["Button_bar"]["pady"],
            columnspan=config["Button_bar"]["columnspan"],
            sticky="w",
        )

        # Erase button customers
        self.erase_button_zak = ctik.CTkButton(
            self.cus_button_frame,
            text="Vymazat",
            command=lambda master=self.tabview.cellfield1: f.clear_cells(master),
        )
        self.erase_button_zak.grid(
            row=0,
            column=2,
            padx=config["Button_bar"]["padx"],
            pady=config["Button_bar"]["pady"],
            columnspan=config["Button_bar"]["columnspan"],
            sticky="e",
        )

        # Erase button reservations
        self.erase_button_res = ctik.CTkButton(
            self.res_button_frame,
            text="Vymazat",
            command=lambda master=self.tabview.reserv1: f.clear_cells(master),
        )
        self.erase_button_res.grid(
            row=0,
            column=4,
            padx=config["Button_bar"]["padx"],
            pady=config["Button_bar"]["pady"],
            columnspan=config["Button_bar"]["columnspan"],
            sticky="w",
        )

        # Placing buttons to convert stickers to txt
        # Placing convert to txt customer button
        self.zak_to_txt = ctik.CTkButton(
            self.cus_button_frame,
            text="Do TXT",
            command=lambda submaster=self.stickerframe: p.stickers_to_txt(submaster),
        )
        self.zak_to_txt.grid(
            row=0,
            column=1,
            padx=config["Button_bar"]["padx"],
            pady=config["Button_bar"]["pady"],
            columnspan=config["Button_bar"]["columnspan"],
            sticky="w",
        )

        # Placing convert to txt reservation button
        self.res_to_txt = ctik.CTkButton(
            self.res_button_frame,
            text="Do TXT",
            command=lambda submaster=self.stickerframe: p.stickers_to_txt(submaster),
        )
        self.res_to_txt.grid(
            row=0,
            column=1,
            padx=config["Button_bar"]["padx"],
            pady=config["Button_bar"]["pady"],
            columnspan=config["Button_bar"]["columnspan"],
            sticky="w",
        )

        # Placing list of sellers for reservations
        self.seller_list = sellers.SellerList(self.res_button_frame)
        self.seller_list.grid(
            row=0,
            column=2,
            padx=config["Button_bar"]["padx"],
            pady=config["Button_bar"]["pady"],
            columnspan=config["Button_bar"]["columnspan"],
        )

        # Placing button for reservation formatting
        self.format_button_res = ctik.CTkButton(
            self.res_button_frame,
            text="Format",
            command=lambda master=self.tabview.reserv1, submaster=self.stickerframe, seller=self.seller_list: ev.res_format_handler(
                master, submaster, seller
            ),
        )
        self.format_button_res.grid(
            row=0,
            column=0,
            padx=config["Button_bar"]["padx"],
            pady=config["Button_bar"]["pady"],
            columnspan=config["Button_bar"]["columnspan"],
            sticky="w",
        )

    def restart(self):
        self.destroy()
        app = App()
        app.mainloop()


def check_version():
    try:
        response = requests.get(API_SOURCE)
        response = response.json()
        active_version = response[0]['tag_name'].lstrip('v')
        if active_version > APP_VERSION:
            print(f"{active_version} is newer than {APP_VERSION}")
            update_app(response)
        else:
            print("You are on the latest version")
    except KeyError as e:
        print(f"Failed to load current version.\n{e}")

def update_app(source):
    download_url = source[0]["assets"][0]["browser_download_url"]
    response = requests.get(download_url)
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        z.extractall()



if __name__ == "__main__":
    check_version()
    app = App()
    app.mainloop()
