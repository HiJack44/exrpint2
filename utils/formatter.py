# this set of functions will format the text from cells and send them to the sticker labels
from constants import auc
from config import config
from widgets import sticker as s
import datetime

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

#This function commands all other formating functions
def format_master(checkedboxes, master, submaster):
    cells_to_format = get_checked_cols(checkedboxes, master)
    cells_to_format = bracket_removal(cells_to_format)
    rows = row_sorter(cells_to_format)
    rows = line_splitter(rows)
    rows = line_limitter(rows, config['Format']['max_str_len'])
    rows = add_date(rows)
    #rows = line_sorter(rows, config['Format']['line_count'])
    label_killer(submaster)
    label_filler(submaster, rows)

# This method takes data from columns that are checked and puts them into dict of lists according to column
def get_checked_cols(checkedboxes, master):
    cells = master.cells
    cells_to_format = {}
    for col in cells:
        print(f"In all {col}")
        if col in checkedboxes:
            for cell, i in enumerate(cells[col]):
                if col not in cells_to_format:
                    cells_to_format[col] = []
                cells_to_format[col].append(cells[col][cell].get("0.0", "end"))
    print(f"Cells to format from get_checke_cols:\n {cells_to_format}")

    return cells_to_format


# Let's use this function in the end, when everything is in rows dictionary rather than cols
def row_sorter(cells: list | dict):
    #print(cells)
    rows = {}
    for i, col in enumerate(cells):
        for j, item in enumerate(cells[col]):
            if j not in rows:
                text_to_dict = item
                rows[j] = text_to_dict
            else:
                text_to_dict = rows[j] + item
                rows[j] = text_to_dict
            # print(f"j = {j}, item = {item}, col = {col}, i = {i}\n text = {rows[j]}")
    print(f"Rows after row sorter:\n{rows}")
    return rows


# This function removes brackets and returns list of rows
def bracket_removal(cells: list | dict):
    if config["Format"]["brackets"] == 1:
        print("Bracket formating acivated")
        for col in cells:
            for i, item in enumerate(cells[col]):
                print(item)
                item = item.replace("(", "\n")
                item = item.replace(" \n", "\n")
                item = item.replace(")", "")
                cells[col][i] = item
    return cells


# this method will generate labels and fill them with rows
def label_filler(master, rows: list | dict):
    master.stickers = {}
    for i, row in enumerate(rows):
        text = rows[i]
        # This IF removes the last return in a string
        if text[-1] == "\n":
            text = text[:-1]
        #text = f"{text[:10]}..\n"
        sticker = s.Sticker(master=master, text=text, justify="left")
        sticker.grid(row=i, column=2, pady=1)
        master.stickers[i] = sticker


# This will erase existing stickers from stickerframe
def label_killer(master):
    try:
        if master.stickers:
            for i, label in enumerate(master.stickers):
                master.stickers[i].destroy()
        else:
            print(f"No stickers in {master}")
    except AttributeError:
        print(f"AttributeError - {master} is empty or has no stickers")

#This method will put rows into lists
def line_splitter(rows):
    for i in rows:
        rows[i] = rows[i][:-1]
        rows[i] = rows[i].split("\n")
        print(f"Row {i} in line_spliter:{rows[i]}")
    print(f"Rows in line_splitter: {rows}")
    return rows

#This function limits the lenght of an item
def line_limitter(rows, lim):
    for row in rows:
        for i, item in enumerate(rows[row]):
            print(f"Item in line_limitter: {item}")
            item = (item[:lim]  + ".." if len(item) > lim else item)
            rows[row][i] = item
            print(f"New item: {item}")
    return rows

#This just adds current date to the item
def add_date(rows):
    if config['Format']['date'] == 1:
        for row in rows:
            item = rows[row][0]
            date = datetime.datetime.now()
            date = date.strftime("%d-%m")
            item = f"{item} | {date}"
            rows[row][0] = item
    return rows

#This function will sort rows into lines for label_printer
def liner_sorter(rows):
    pass