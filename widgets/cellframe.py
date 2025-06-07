#frame for cells

import customtkinter as ctik
from widgets import cell
from constants import auc

class Cellframe(ctik.CTkScrollableFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.c_width = 40
        self.c_height = 1

        self.cells = {}
        for col in range(9):
            col_letter = auc[col]

            if col_letter not in self.cells:
                self.cells[col_letter] = []
            for row in range(10):
                uid = f"{col_letter}{row}"

                cl = cell.Cell(self, row, col, width=self.c_width, height=self.c_height)
                cl.grid(row=row, column=col,padx=1,pady=1)

                row += 1
            col += 1



