import customtkinter as ctik
from widgets import cell, sticker, cellframe, tab

#Main function of the program
class App(ctik.CTk):
    def __init__(self):
        super().__init__()

        #Defining the window
        self.geometry("800x600")
        self.title("Exprint 2")
        ctik.set_default_color_theme("templates/theme_dark.json")
        self.grid_columnconfigure((0,1),weight=1)

        #placing of the cellframe to the window
        #cellfield1 = cellframe.Cellframe(self,width=400)
        #cellfield1.grid(row=0, column=0)

        tabview = tab.Tab(self)
        tabview.grid(row=0, column=0)

        self.sticker1 = sticker.Sticker(self)
        self.sticker1.grid(row=0, column=1)



app = App()
app.mainloop()
