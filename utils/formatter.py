# this set of functions will format the text from cells and send them to the sticker labels
from datetime import timedelta

from constants import auc
from config import config
from widgets import sticker as s
from widgets import alertwindow as alwi
import datetime
import re


# Function to clear all the cells
def clear_cells(master):
    try:
        for col, i in enumerate(master.cells):
            col_letter = auc[col]
            for row, j in enumerate(master.cells[col_letter]):
                master.cells[col_letter][row].delete("0.0", "end")
                # print(f"Cell {col_letter}{row} erased")
        print("All cells were erased")
    except:
        print("Erase failed")
    return "break"


# This function commands all other formating functions
def format_master(checkedboxes, master, submaster):
    rows = ""
    cells_to_format = ""
    label_killer(submaster)
    cells_to_format = get_checked_cols(checkedboxes, master)
    cells_to_format = piece_sign_adder(cells_to_format)
    cells_to_format = money_sign_adder(cells_to_format)
    cells_to_format = bracket_removal(cells_to_format)
    rows = row_sorter(cells_to_format)
    rows = line_splitter(rows)
    rows = line_limitter(rows, config["Format"]["max_str_len"])
    rows = add_date(rows, 0)
    rows = line_sorter(rows, config["Format"]["line_count"])
    # print(rows)
    # label_killer(submaster)
    label_filler(submaster, rows)


# This method takes data from columns that are checked and puts them into dict of lists according to column
def get_checked_cols(checkedboxes, master):
    if len(checkedboxes) != config["Format"]["line_count"]:
        error_msg = f"Nesprávný počet sloupců!\nPočet sloupců musí být přesně {config['Format']['line_count']}"
        line_count_error = alwi.open_alert(master, "Nesprávný počet sloupců", error_msg)
        raise IndexError
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
    # print(cells)
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
    if int(config["Format"]["brackets"]) == 1:
        for col in cells:
            for i, item in enumerate(cells[col]):
                item = item.replace("(", "\n", 1)
                item = item.replace(" \n", "\n")
                item = item.replace(")", "", -1)
                cells[col][i] = item
    return cells


# this method will generate labels and fill them with rows
def label_filler(master, rows: list | dict):
    print(f"Rows in label_filler\n{rows}")
    master.stickers = {}
    for i, row in enumerate(rows):
        if i in rows:
            text = rows[i]
            # This IF removes the last return in a string
            try:
                if text[-1] == "\n":
                    text = text[:-1]
                sticker = s.Sticker(master=master, text=text, justify="left")
                sticker.grid(row=i, column=1, pady=1)
                master.stickers[i] = sticker
            except IndexError as e:
                print(f"Index error, asi nic inside: {e}")


# This will erase existing stickers from stickerframe
def label_killer(master):
    try:
        if master.stickers:
            print(
                f"Lenght of master.stickers before killer: {len(master.stickers)} \n {master.stickers}"
            )
            for i, label in enumerate(master.stickers):
                if i in master.stickers:
                    master.stickers[i].destroy()
            print(
                f"Lenght of master.stickers after killer: {len(master.stickers)} \n {master.stickers}"
            )

        else:
            print(f"No stickers in {master}")
    except AttributeError:
        print(f"AttributeError - {master} is empty or has no stickers")
    except KeyError as ke:
        print(f"KeyError {ke}. Skipping number {i}")
        # i += 1


# This method will put rows into lists
def line_splitter(rows):
    offset_value = 0
    # Check if row is empty and add count to offset counter, if there is an empty line, offset the next full one there
    for i in list(rows):
        if "\n\n\n" in rows[i]:
            offset_value += 1
        else:
            rows[i] = rows[i][:-1]
            rows[i - offset_value] = rows[i].split("\n")
            print(f"Row {i} in line_spliter:{rows[i]}")
    # Delete empty rows
    for i in list(rows):
        if "\n\n\n" in rows[i]:
            del rows[i]
    # Delete nn empty rows that didn't get formated and got doubled
    for i in list(rows):
        if not isinstance(rows[i], list):
            del rows[i]
    print(f"Offset value = {offset_value}")
    print(f"Rows in line_splitter: {rows}")
    return rows


# This function limits the lenght of an item
def line_limitter(rows, lim):
    print(f"Rows in line_limitter:\n{rows}")
    try:
        for row in rows:
            for i, item in enumerate(rows[row]):
                print(f"Item in line_limitter: {type(item)}{item} into {rows[row]}")
                item = item[:lim] + ".." if len(item) > lim else item
                rows[row][i] = item
                print(f"New item: {item}")
    except TypeError as te:
        print(f"Ooops, {te}")
        return None
    return rows


# This just adds current date to the item
def add_date(rows, offset):
    if int(config["Format"]["date"]) == 1:
        for row in rows:
            item = rows[row][0]
            date = datetime.datetime.now() + timedelta(offset)
            date = date.strftime("%d-%m")
            if offset > 0:
                item = f"{item} | do: {date}"
            else:
                item = f"{item} | {date}"
            rows[row][0] = item
    return rows


# This function will sort rows into lines for label_printer
def line_sorter(rows, lim):
    stickers_content = {}
    for i, row in enumerate(rows):
        if i in rows:
            if i not in stickers_content:
                stickers_content[i] = "--"
            try:
                for j, item in enumerate(rows[i]):
                    match j:
                        case 0:
                            stickers_content[i] = item
                        case 1 | 2 | 3 | 4:
                            stickers_content[i] = stickers_content[i] + "\n" + item
                        case 5:
                            stickers_content[i] = stickers_content[i] + "|" + item
                        case _:
                            print("Too many lines")
            except KeyError as e:
                print(f"Key error {e}")
    print(stickers_content)
    return stickers_content


# This function adds piece sign to a specific column
def piece_sign_adder(cells: list | dict):
    if int(config["Format"]["pieces"]) == 1:
        print("Piece sign activated")
        for col in cells:
            for i, item in enumerate(cells[col]):
                if col == config["Format"]["pieces_col"]:
                    item = "|ks: " + item
                    cells[col][i] = item
    return cells


# This function adds currency sign to a specific column
def money_sign_adder(cells: list | dict):
    if int(config["Format"]["money_sign"]) == 1:
        print("Currency sign activated")
        for col in cells:
            for i, item in enumerate(cells[col]):
                if col == config["Format"]["money_sign_col"]:
                    item = config["Format"]["active_money_sign"] + item
                    cells[col][i] = item
    return cells


# This function will control formatting of reservation tab
def reservation_formatter(master, submaster, rows, seller):
    rows_to_format = []
    rows = master.cells["B"]
    print(f"Rows in reservation_formatter before loop:\n{rows}")
    for i, cell in enumerate(rows):
        if i in config["Rezervace"]["format_rows"]:
            rows_to_format.append(cell.get("0.0", "end"))
    label_killer(submaster)
    rows_to_format.insert(0, seller)
    rows_to_format = {0: rows_to_format}
    print(f"Rows to format after loop:\n{rows_to_format}")
    rows_to_format = break_remover(rows_to_format)
    rows_to_format = space_remover(rows_to_format)
    rows_to_format = line_limitter(rows_to_format, config["Format"]["max_str_len"])
    rows_to_format = add_date(rows_to_format, config["Rezervace"]["until"])
    rows_to_format = line_sorter(rows_to_format, config["Format"]["line_count"])
    label_filler(submaster, rows_to_format)


# This function removes new line at the end of cell
def break_remover(cells: list | dict):
    for i, row in enumerate(cells[0]):
        print(f"Cell {cells[0][i]} in break_remover")
        if cells[0][i][-1] == "\n":
            cells[0][i] = cells[0][i][:-1]
    return cells


# This function remove one space at the beggining of a cell
def space_remover(cells: list | dict):
    for i, row in enumerate(cells[0]):
        cells[0][i] = cells[0][i].strip()
    return cells
