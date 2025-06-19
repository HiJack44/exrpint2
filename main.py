import customtkinter as ctik
from widgets import cell, sticker, tab
from utils import formatter as f

#Main function of the program
class App(ctik.CTk):
    def __init__(self):
        super().__init__()

        #Defining the window
        self.geometry("800x600")
        self.title("Exprint 2")
        ctik.set_default_color_theme("templates/theme_dark.json")
        self.grid_columnconfigure((0,1),weight=1)

        #Placing the tabview with cellframes
        self.tabview = tab.Tab(self)
        self.tabview.grid(row=1, column=0)

        self.sticker1 = sticker.Sticker(self)
        self.sticker1.grid(row=1, column=1)

        #Placing buttons
        self.format_button = ctik.CTkButton(self, text="Format", command=lambda: f.pritn_all_cells(self.tabview.cellfield1))
        self.format_button.grid(row=0, column=0, padx=1, pady=1)



app = App()
app.mainloop()
