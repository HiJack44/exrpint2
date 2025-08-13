# This is the settings window that will allow the user to customize the app

import customtkinter as ctik
import json, os


from config import config
from config import save_config as sc
from widgets import settinglabel as sl
from widgets import sellermanager as sm


class Settings(ctik.CTkToplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # path = os.path.join("templates", "config.json")

        self.geometry("500x500")
        self.title("Nastavení")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(1, weight=1)

        data = config
        cellfieldpath = parent.tabview.cellfield1
        self.alert_window = None

        self.sellermanager = None

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

        # Date adder
        date_adder_var = ctik.StringVar(value=config["Format"]["date"])
        self.date_adder_label = sl.MenuItem(
            master=self.general_settings_frame, text="Datum", anchor="w"
        )
        self.date_adder_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.date_adder_switch = ctik.CTkSwitch(
            self.general_settings_frame,
            text="",
            variable=date_adder_var,
            onvalue="1",
            offvalue="0",
        )
        self.date_adder_switch.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        """"CUSTOMERS SETTING SECTION"""
        """"This section is for setup of the Customers window"""
        self.cus_settings_frame.grid_columnconfigure(1, weight=1)

        # Currency switch
        money_sign_switch_var = ctik.StringVar(value=config["Format"]["money_sign"])
        self.money_sign_switch_label = sl.MenuItem(
            master=self.cus_settings_frame, text="Měna"
        )
        self.money_sign_switch_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
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
        self.money_sign_list_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.money_sign_list = ctik.CTkOptionMenu(
            self.cus_settings_frame,
            width=60,
            variable=money_sign_list_var,
            values=config["Format"]["money_sign_list"],
        )
        self.money_sign_list.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Currency sign colum selector
        self.money_col_label = sl.MenuItem(
            master=self.cus_settings_frame, text="Sloupec měny"
        )
        self.money_col_label.grid(row=3, column=0, pady=5, padx=5, sticky="w")

        checkboxes = list(
            cellfieldpath.checkboxes.keys()
        )  # Getting list of existing columns
        money_col_var = ctik.StringVar(value=config["Format"]["money_sign_col"])
        self.money_col_list = ctik.CTkOptionMenu(
            self.cus_settings_frame, width=60, variable=money_col_var, values=checkboxes
        )
        self.money_col_list.grid(row=3, column=1, pady=5, padx=5, sticky="w")

        # Bracket remover
        bracket_remover_var = ctik.StringVar(value=config["Format"]["brackets"])

        self.bracket_remover_label = sl.MenuItem(master=self.cus_settings_frame, text="Závorkovač")
        self.bracket_remover_label.grid(row=4, column=0, pady=5, padx=5, sticky='w')

        self.bracket_remover_switch = ctik.CTkSwitch(self.cus_settings_frame, text="", variable=bracket_remover_var, onvalue="1", offvalue="0" )
        self.bracket_remover_switch.grid(row=4, column=1, padx=5, pady=5, sticky='w')

        """"RESERVATION SETTINGS SECTION"""
        """This section is for reservation settings"""

        # Reservation time - days until reservation expires
        # Function to display current state of the slider
        def slidernumber(value):
            days = self.until_days_slider.get()
            self.until_days_current.configure(text=int(days))

        until_days_var = ctik.IntVar(value=config["Rezervace"]["until"])
        self.until_days_label = sl.MenuItem(self.res_settings_frame, text="Počet dní")
        self.until_days_label.grid(row=1, column=0, pady=5, padx=5, sticky="w")

        self.until_days_slider = ctik.CTkSlider(
            self.res_settings_frame,
            from_=0,
            to=7,
            number_of_steps=7,
            width=150,
            variable=until_days_var,
            command=slidernumber,
        )
        self.until_days_slider.grid(row=1, column=1, pady=(5,0), padx=5, sticky="w")

        self.until_days_current = sl.MenuItem(
            self.res_settings_frame, text=until_days_var.get()
        )
        self.until_days_current.grid(row=2, column=1, padx=5, pady=(0,5), sticky="ew")

        #Seller list with add/remove buttons in column 3
        self.seller_list_label = sl.MenuItem(self.res_settings_frame, text="Seznam prodejců")
        self.seller_list_label.grid(row=3, column=0, pady=5, padx=5, sticky='w')

        self.seller_list_menu = ctik.CTkOptionMenu(self.res_settings_frame, values=config['Rezervace']['sellers'])
        self.seller_list_menu.grid(row=3, column=1, pady=5, padx=5, sticky='w')

        # This button opens a new window with option to add new or remove some sellers
        self.seller_list_button = ctik.CTkButton(self.res_settings_frame, text="+/-", width=20, fg_color='transparent',
                                                 command=lambda parent=self: sm.open_seller_manager(parent))
        self.seller_list_button.grid(row=3, column=2, padx=(0,5), pady=5, sticky='w')


    """General methods and functions of the settings class"""
    #This function just closes the settings window
    def close_settings(self):
        self.destroy()

    #This function saves all the settings by rewriting config.json
    def save_settings(self, data):
        data["Format"]["money_sign"] = self.money_sign_switch.get()
        data["Format"]["active_money_sign"] = self.money_sign_list.get()
        data["Format"]["date"] = self.date_adder_switch.get()
        data["Format"]["money_sign_col"] = self.money_col_list.get()
        data["Format"]["brackets"] = self.bracket_remover_switch.get()
        data["Rezervace"]["until"] = self.until_days_slider.get()

        sc(data)
        self.close_settings()

# This is super necessary
def open_settings(parent):
    if parent.settings is None or not parent.settings.winfo_exists():
        parent.settings = Settings(parent)
    else:
        parent.settings.focus()
