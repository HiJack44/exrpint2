import customtkinter as ctik
from widgets import cell

class App(ctik.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x600")
        self.title("Exprint 2")
        ctik.set_default_color_theme("templates/theme_dark.json")

        self.cell1 = cell.Cell(self, width=80, height=12)
        self.cell1.grid(row=0, column=0)



app = App()
app.mainloop()
