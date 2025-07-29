import customtkinter as ctik
from widgets import stickerframe, tab, sellers
from utils import events as ev
from utils import formatter as f
from utils import print as p
from config import config


# Main function of the program
class App(ctik.CTk):
    def __init__(self):
        super().__init__()

        # Defining the window
        self.geometry("1250x700")
        self.minsize(1250, 700)
        self.title("Exprint 2")
        try:
            ctik.set_default_color_theme("templates/theme_dark.json")
        except:
            print("Failed to load theme")
        self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)

        # Placing the tabview with cellframes
        self.tabview = tab.Tab(self)
        self.tabview.grid(row=0, column=0, padx=(5, 0), sticky="nsw")

        # Placing stickerframe which will be displaying formated stickers
        self.stickerframe = stickerframe.Stickerframe(self, width=280, height=600)
        self.stickerframe.grid(row=0, column=1, padx=5, pady=5, sticky="sew")

        # Placing frame for customers buttons
        self.cus_button_frame = ctik.CTkFrame(
            self.tabview.cellfield1, fg_color="lightblue"
        )
        self.cus_button_frame.grid(row=0, column=0, sticky="we", columnspan=10)
        self.cus_button_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # Placing frame for buttons for reservations
        self.res_button_frame = ctik.CTkFrame(
            self.tabview.reserv1, fg_color="lightblue"
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
            column=1,
            padx=config["Button_bar"]["padx"],
            pady=config["Button_bar"]["pady"],
            columnspan=config["Button_bar"]["columnspan"],
        )

        # Placing button to convert stickers to txt
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

        # Placing button for reservation formatting
        self.format_button_res = ctik.CTkButton(self.res_button_frame, text="Format")
        self.format_button_res.grid(
            row=0,
            column=0,
            padx=config["Button_bar"]["padx"],
            pady=config["Button_bar"]["pady"],
            columnspan=config["Button_bar"]["columnspan"],
        )

        #Placing list of sellers for reservations
        seller_list = sellers.SellerList(self.res_button_frame)
        seller_list.grid(
            row=0,
            column=3,
            padx=config["Button_bar"]["padx"],
            pady=config["Button_bar"]["pady"],
            columnspan=config["Button_bar"]["columnspan"]
        )


app = App()
app.mainloop()
