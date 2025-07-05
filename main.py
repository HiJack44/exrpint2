import customtkinter as ctik
from widgets import cell, sticker, tab
from utils import events as ev
from utils import formatter as f


# Main function of the program
class App(ctik.CTk):
    def __init__(self):
        super().__init__()

        # Defining the window
        self.geometry("1200x600")
        self.title("Exprint 2")
        try:
            ctik.set_default_color_theme("templates/theme_dark.json")
        except:
            print("Failed to load theme")
        self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)

        # Placing the tabview with cellframes
        self.tabview = tab.Tab(self)
        self.tabview.grid(row=0, column=0, sticky="nsw")

        self.sticker1 = sticker.Sticker(self)
        self.sticker1.grid(row=0, column=1)

        # Placing buttons
        # Format Button
        self.format_button = ctik.CTkButton(
            self.tabview.cellfield1,
            text="Format",
            command=lambda master = self.tabview.cellfield1: ev.format_handler(master)
        )
        self.format_button.grid(
            row=0, column=0, padx=1, pady=1, columnspan=10, sticky="w"
        )

        # Erase button customers
        self.erase_button_zak = ctik.CTkButton(
            self.tabview.cellfield1,
            text="Vymazat",
            command=lambda master=self.tabview.cellfield1: f.clear_cells(master),
        )
        self.erase_button_zak.grid(row=0, column=6, columnspan = 3, sticky="e")

        #Erase button reservations
        self.erase_button_zak = ctik.CTkButton(
            self.tabview.reserv1,
            text="Vymazat",
            command=lambda master=self.tabview.reserv1: f.clear_cells(master),
        )
        self.erase_button_zak.grid(row=0, column=1, sticky='e')


app = App()
app.mainloop()
