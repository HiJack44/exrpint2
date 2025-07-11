# this set of functions will format the text from cells and send them to the sticker labels
import pyperclip as pc

from constants import auc
from config import config
#from widgets import stickerframe as sf
from widgets import sticker as s

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

#This method takes data from columns that are checked and puts them into dict of lists according to column
def get_checked_cols(checkedboxes, master, submaster):
    cells = master.cells
    cells_to_format = {}
    for col in cells:
        print(f"In all {col}")
        if col in checkedboxes:
            for cell, i in enumerate(cells[col]):
                if col not in cells_to_format:
                    cells_to_format[col] = []
                cells_to_format[col].append(cells[col][cell].get('0.0', "end"))
    row_sorter(cells_to_format, submaster)
#Let's use this function in the end, when everything is in rows dictionary rather than cols
def row_sorter(cells: list|dict, submaster):
    print(cells)
    rows = {}
    for i, col in enumerate(cells):
        if config['Format']['brackets'] == 1:
            print("Bracket formating acivated")
            cells[col] = bracket_removal(cells[col])
        print(f"Cells after bracket removal:\n{cells}")
        for j, item in enumerate(cells[col]):
            if j not in rows:
                text_to_dict = item
                rows[j] = text_to_dict
            else:
                text_to_dict = rows[j] + item
                rows[j] = text_to_dict
            #print(f"j = {j}, item = {item}, col = {col}, i = {i}\n text = {rows[j]}")
    #app.sticker_dropper(rows)
    label_filler(submaster, rows)
    print(f"Rows after row sorter:\n{rows}")
#This function removes brackets and returns list of rows
def bracket_removal(cells: list|dict):
    for i, item in enumerate(cells):
        print(item)
        item = item.replace("(", "\n")
        item = item.replace(" \n", "\n")
        item = item.replace(")", "")
        cells[i] = item
        #cells[i] = item.replace("\n\n", "")
        #cells[i] = item.replace("\n", "")
        #cells[i] = cells[i].split("\n")
        print("Delka textu" + str(len(item)))
        print(f"Brackets removed. New item: {item}")
    return cells

#this method will generate labels and fill them with rows
def label_filler(master, rows: list|dict):

    for i, row in enumerate(rows):
        text = rows[i]
        # This IF removes the last return in a string
        if text[-1] == "\n":
            text = text[:-1]
        sticker = s.Sticker(master=master, text=text, justify='left')
        sticker.grid(row=i, column=2, pady=1)
