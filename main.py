import customtkinter as ctik
from widgets import cell, sticker, tab
from utils import formatter as f

#Main function of the program
class App(ctik.CTk):
    def __init__(self):
        super().__init__()

        #Defining the window
        self.geometry("1200x600")
        self.title("Exprint 2")
        try:
            ctik.set_default_color_theme("templates/theme_dark.json")
        except:
            print("Failed to load theme")
        self.grid_columnconfigure((0,1),weight=1)
        #self.grid_rowconfigure(0, weight=1)

        #Placing the tabview with cellframes
        self.tabview = tab.Tab(self)
        self.tabview.grid(row=0, column=0, sticky='nsw')

        self.sticker1 = sticker.Sticker(self)
        self.sticker1.grid(row=0, column=1)

        #Placing buttons
        self.format_button = ctik.CTkButton(self.tabview.cellfield1, text="Format", command=lambda: f.pritn_all_cells(self.tabview))
        self.format_button.grid(row=0, column=0, padx=1, pady=1, columnspan=10, sticky='w')



app = App()
app.mainloop()
