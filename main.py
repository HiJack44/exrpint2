import customtkinter as ctik
from widgets import cell, sticker, cellframe

class App(ctik.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x600")
        self.title("Exprint 2")
        ctik.set_default_color_theme("templates/theme_dark.json")
        #self.grid_columnconfigure(0,weight=1)

        #self.cell1 = cell.Cell(self, width=80, height=12)
        #self.cell1.grid(row=0, column=0)
        cellfield1 = cellframe.Cellframe(self,width=400)
        cellfield1.grid(row=0, column=0)

        self.sticker1 = sticker.Sticker(self)
        self.sticker1.grid(row=0, column=1)



app = App()
app.mainloop()
