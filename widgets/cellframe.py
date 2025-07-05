# frame for the cell deployment

import customtkinter as ctik
from widgets import cell
from constants import auc
from utils import events as evn
import clipboard as clip

# Cellframe class to spawn the cells
class Cellframe(ctik.CTkScrollableFrame):
    def __init__(self, master, row_count, col_count, cw, ch, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        #Grid configuration
        #self.grid_rowconfigure((0,1), weight=1)
        #self.grid_columnconfigure((0,7), weight=1)
        #Amount of rows and columns
        self.row_count = row_count
        self.col_count = col_count

        # width and height of the cells
        self.c_width = cw
        self.c_height = ch

        # dictionary that wraps the cells
        self.cells = {}
        self.checkboxes = {}

        # cell generation loop
        for col in range(col_count):

            # Renaming of the column number to letter.
            # Letter is used with row number to adress the cell
            col_letter = auc[col]
            self.letter_checkbox = ctik.CTkCheckBox(self, text=col_letter, checkbox_width=15, checkbox_height=15)
            self.letter_checkbox.grid(row=1, column=col, sticky='w')
            if col_letter not in self.checkboxes:
                self.checkboxes[col_letter] = self.letter_checkbox


            # if to check if column already exists, if not: create it
            if col_letter not in self.cells:
                self.cells[col_letter] = []

            # row and cell generation
            for row in range(row_count):
                uid = f"{col_letter}{row}"

                # Creation of the cell widget from the Cell class in the cell.py
                cl = cell.Cell(
                    self, row, col_letter, width=self.c_width, height=self.c_height
                )
                cl.grid(row=row+3, column=col, padx=1, pady=0.1, sticky='ew')
                self.grid_columnconfigure(col, weight=1)

                # Addition of the cell to the cells dictionary
                self.cells[col_letter].append(cl)

                # Binding the keys to functions
                downkeys = ["<Return>", "<Down>", "KP_Enter"]
                rightkeys = ["<Right>", "<Tab>"]

                # Down movement
                for key in downkeys:
                    self.cells[col_letter][row].bind(
                        key,
                        lambda event, master=self, row=row + 1, col=col_letter: evn.next_cell(
                            event, master, col, row
                        ),
                    )
                # Right movement
                for key in rightkeys:
                    self.cells[col_letter][row].bind(
                        key,
                        lambda event, master=self, row=row, col=auc[
                            col + 1
                        ]: evn.next_cell(event, master, col, row),
                    )

                # Left movement
                self.cells[col_letter][row].bind(
                    "<Left>",
                    lambda event, master=self, row=row, col=auc[col - 1]: evn.next_cell(
                        event, master, col, row
                    ),
                )
                # Up movement
                self.cells[col_letter][row].bind(
                    "<Up>",
                    lambda event, master=self, row=row - 1, col=auc[col]: evn.next_cell(
                        event, master, col, row
                    ),
                )
                #Copy ctrl+c keys binding
                self.cells[col_letter][row].bind("<Control-c>", evn.custom_copy)
                # Paste ctrl+v keys binding
                try:
                    self.cells[col_letter][row].bind("<Control-v>", lambda event, master = self, col = col, row=row:
                    evn.paste_data_to_cells(event, master, col, row))
                except:
                    print("Cant control v")

                row += 1
            col += 1

            # Focus on first cell after loading the program
            self.cells["A"][0].focus_set()