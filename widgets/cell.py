import customtkinter as ctik

#class that defines individual cell
class Cell(ctik.CTkTextbox):
    def __init__(self, master, row, column, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.row = row
        self.column = column