# This is the settings window that will allow the user to customize the app

import customtkinter as ctik
import json, os
from constants import auc


from config import config
from config import save_config as sc
from widgets import settinglabel as sl
from widgets import sellermanager as sm
from widgets import spinbox


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

        # Line limiter - this will limit the lenght of each line
        def strlennumber(value):
            strlen = self.line_limiter_slider.get()
            self.line_limiter_current_label.configure(text=int(strlen))

        line_limiter_var = ctik.IntVar(value=config["Format"]["max_str_len"])

        self.line_limiter_label = sl.MenuItem(
            self.general_settings_frame, text="Max. délka textu"
        )
        self.line_limiter_label.grid(row=1, column=0, padx=5, pady=(5, 0), sticky="w")

        self.line_limiter_slider = ctik.CTkSlider(
            self.general_settings_frame,
            from_=5,
            to=15,
            number_of_steps=10,
            width=150,
            variable=line_limiter_var,
            command=strlennumber,
        )
        self.line_limiter_slider.grid(row=1, column=1, padx=5, pady=(5, 0), sticky="w")

        self.line_limiter_current_label = sl.MenuItem(
            self.general_settings_frame, text=line_limiter_var.get()
        )
        self.line_limiter_current_label.grid(
            row=2, column=1, padx=5, pady=(0, 5), sticky="ew"
        )

        # Date adder
        date_adder_var = ctik.StringVar(value=config["Format"]["date"])
        self.date_adder_label = sl.MenuItem(
            master=self.general_settings_frame, text="Datum", anchor="w"
        )
        self.date_adder_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.date_adder_switch = ctik.CTkSwitch(
            self.general_settings_frame,
            text="",
            variable=date_adder_var,
            onvalue="1",
            offvalue="0",
        )
        self.date_adder_switch.grid(row=3, column=1, padx=5, pady=5, sticky="w")

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

        self.bracket_remover_label = sl.MenuItem(
            master=self.cus_settings_frame, text="Závorkovač"
        )
        self.bracket_remover_label.grid(row=4, column=0, pady=5, padx=5, sticky="w")

        self.bracket_remover_switch = ctik.CTkSwitch(
            self.cus_settings_frame,
            text="",
            variable=bracket_remover_var,
            onvalue="1",
            offvalue="0",
        )
        self.bracket_remover_switch.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        # Piece sign adder
        piece_sign_adder_var = ctik.StringVar(value=config["Format"]["pieces"])

        self.piece_sign_adder_label = sl.MenuItem(
            self.cus_settings_frame, text="Kusovník"
        )
        self.piece_sign_adder_label.grid(row=5, column=0, pady=5, padx=5, sticky="w")

        self.piece_sign_adder_switch = ctik.CTkSwitch(
            self.cus_settings_frame,
            text="",
            variable=piece_sign_adder_var,
            onvalue="1",
            offvalue="0",
        )
        self.piece_sign_adder_switch.grid(row=5, column=1, pady=5, padx=5, sticky="w")

        # Piece sign column selector
        piece_sign_col_var = ctik.StringVar(value=config["Format"]["pieces_col"])

        self.piece_sign_col_label = sl.MenuItem(
            self.cus_settings_frame, text="Sloupec kusovníku"
        )
        self.piece_sign_col_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")

        self.piece_sign_col_list = ctik.CTkOptionMenu(
            self.cus_settings_frame,
            width=60,
            variable=piece_sign_col_var,
            values=checkboxes,
        )
        self.piece_sign_col_list.grid(row=6, column=1, padx=5, pady=5, sticky="w")

        # Row count - setting up amount of rows in the Customers tab
        self.cells_rows_label = sl.MenuItem(self.cus_settings_frame, text="Počet řádků")
        self.cells_rows_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")

        self.cell_rows_spinbox = spinbox.Spinbox(
            self.cus_settings_frame, value=config["Zakaznici"]["row_count"]
        )
        self.cell_rows_spinbox.grid(row=7, column=1, padx=5, pady=5, sticky="w")

        # Column count - setting up the amount of columns in the cell grid
        self.cells_column_label = sl.MenuItem(self.cus_settings_frame, "Počet sloupců")
        self.cells_column_label.grid(row=8, column=0, padx=5, pady=5, sticky="w")

        self.cells_column_spinbox = spinbox.Spinbox(
            self.cus_settings_frame, value=config["Zakaznici"]["column_count"]
        )
        self.cells_column_spinbox.grid(row=8, column=1, padx=5, pady=5, sticky="w")

        # Preset for checked checkboxes on the startup
        # Frame for checkboxes
        self.checkbox_frame = ctik.CTkFrame(
            self.cus_settings_frame,
            fg_color="transparent",
            border_width=1,
            border_color="black",
        )
        self.checkbox_frame.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

        self.checkbox_label = sl.MenuItem(
            self.checkbox_frame, text="Aktivní sloupce - preset"
        )
        self.checkbox_label.grid(row=0, column=0, padx=3, pady=3, columnspan=10)

        self.checkboxes = {}
        col_col = 0
        for col in range(config["Zakaznici"]["column_count"]):
            col_letter = auc[col]
            self.checkbox = ctik.CTkCheckBox(
                self.checkbox_frame,
                text=col_letter,
                checkbox_width=20,
                checkbox_height=20,
                width=20,
            )
            if col_col % 5 == 0:
                col_col = 0
            self.checkbox.grid(
                row=int(col / 5) + 1, column=col_col, padx=3, pady=(3, 5)
            )
            col_col += 1

            # Adding checkboxes to dict for further manipulation
            if col_letter not in self.checkboxes:
                self.checkboxes[col_letter] = self.checkbox
            if col_letter in config["Zakaznici"]["checked_cols"]:
                self.checkbox.select()

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
        self.until_days_slider.grid(row=1, column=1, pady=(5, 0), padx=5, sticky="w")

        self.until_days_current = sl.MenuItem(
            self.res_settings_frame, text=until_days_var.get()
        )
        self.until_days_current.grid(row=2, column=1, padx=5, pady=(0, 5), sticky="ew")

        # Seller list with add/remove buttons in column 3
        self.seller_list_label = sl.MenuItem(
            self.res_settings_frame, text="Seznam prodejců"
        )
        self.seller_list_label.grid(row=3, column=0, pady=5, padx=5, sticky="w")

        self.seller_list_menu = ctik.CTkOptionMenu(
            self.res_settings_frame, values=config["Rezervace"]["sellers"]
        )
        self.seller_list_menu.grid(row=3, column=1, pady=5, padx=5, sticky="w")

        # This button opens a new window with option to add new or remove some sellers
        self.seller_list_button = ctik.CTkButton(
            self.res_settings_frame,
            text="+/-",
            width=20,
            fg_color="transparent",
            command=lambda parent=self: sm.open_seller_manager(parent),
        )
        self.seller_list_button.grid(row=3, column=2, padx=(0, 5), pady=5, sticky="w")

        # Reservation rows amount
        self.res_rows_lable = sl.MenuItem(self.res_settings_frame, text="Počet řádků")
        self.res_rows_lable.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        self.res_rows_spinbox = spinbox.Spinbox(
            self.res_settings_frame, value=config["Rezervace"]["row_count"]
        )
        self.res_rows_spinbox.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    """General methods and functions of the settings class"""

    # This function just closes the settings window
    def close_settings(self):
        self.destroy()

    # This function saves all the settings by rewriting config.json
    def save_settings(self, data):
        data["Format"]["max_str_len"] = int(self.line_limiter_slider.get())
        data["Format"]["money_sign"] = self.money_sign_switch.get()
        data["Format"]["active_money_sign"] = self.money_sign_list.get()
        data["Format"]["date"] = self.date_adder_switch.get()
        data["Format"]["money_sign_col"] = self.money_col_list.get()
        data["Format"]["brackets"] = self.bracket_remover_switch.get()
        data["Format"]["pieces"] = self.piece_sign_adder_switch.get()
        data["Format"]["pieces_col"] = self.piece_sign_col_list.get()
        data["Zakaznici"]["row_count"] = int(self.cell_rows_spinbox.get())
        data["Zakaznici"]["column_count"] = int(self.cells_column_spinbox.get())
        data["Rezervace"]["until"] = int(self.until_days_slider.get())
        data["Rezervace"]["row_count"] = int(self.res_rows_spinbox.get())
        data["Zakaznici"]["checked_cols"] = self.checkbox_checker()

        sc(data)
        self.close_settings()

    # Function for checked checkboxes preset setting
    def checkbox_checker(self):
        checkedboxes = []
        for key in self.checkboxes:
            if self.checkboxes[key].get() == 1:
                checkedboxes.append(key)
        return checkedboxes


# This is super necessary
def open_settings(parent):
    if parent.settings is None or not parent.settings.winfo_exists():
        parent.settings = Settings(parent)
    else:
        parent.settings.focus()
