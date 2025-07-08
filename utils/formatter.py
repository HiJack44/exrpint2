# this set of functions will format the text from cells and send them to the sticker labels
import pyperclip as pc
from constants import auc


def pritn_all_cells(arg):
    # from main import app
    text = arg.cellfield1.cells["A"][1].get_text()
    print(text)

    return "break"


# Function to clear all the cells
def clear_cells(master):
    try:
        for col, i in enumerate(master.cells):
            col_letter = auc[col]
            for row, j in enumerate(master.cells[col_letter]):
                master.cells[col_letter][row].delete("0.0", "end")
                print(f"Cell {col_letter}{row} erased")
        print("All cells were erased")
    except:
        print("Erase failed")
    return "break"

def get_checked_cols(checkedboxes, master):
    cells = master.cells
    cells_to_format = {}
    for col in cells:
        print(f"In all {col}")
        if col in checkedboxes:
            for cell, i in enumerate(cells[col]):
                if col not in cells_to_format:
                    cells_to_format[col] = []
                cells_to_format[col].append(cells[col][cell].get('0.0', "end"))
                #print(cells[col][cell].get('0.0', "end"))
    print(cells_to_format)
    #formattext(cells_to_format)