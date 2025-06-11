# frame for the cell deployment

import customtkinter as ctik
from widgets import cell
from constants import auc
from utils import events as evn


# Cellframe class to spawn the cells
class Cellframe(ctik.CTkScrollableFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # width and height of the cells
        self.c_width = 40
        self.c_height = 1

        # dictionary that wraps the cells
        self.cells = {}

        # cell generation loop
        for col in range(3):

            # Renaming of the column number to letter. Letter is used with row number to adress the cell
            col_letter = auc[col]

            # if to check if column already exists, if not: create it
            if col_letter not in self.cells:
                self.cells[col_letter] = []

            # row and cell generation
            for row in range(2):
                uid = f"{col_letter}{row}"

                # Creation of the cell widget from the Cell class in the cell.py
                cl = cell.Cell(
                    self, row, col_letter, width=self.c_width, height=self.c_height
                )
                cl.grid(row=row, column=col, padx=1, pady=1)

                # Addition of the cell to the cells dictionary
                self.cells[col_letter].append(cl)

                # Binding the keys to functions
                self.cells[col_letter][row].bind("<Return>", evn.next_row)
                self.cells[col_letter][row].bind(
                    "<Tab>",
                    lambda event, master=self, row=row, col=auc[col + 1]: evn.next_cell(
                        event, master, col, row
                    ),
                )
                self.cells[col_letter][row].focus_set()
                self.cells['A'][0].focus_set()

                row += 1
            col += 1
