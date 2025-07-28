# Key-bound events
from constants import auc
from utils import formatter as f
from config import config


# Focus the cell in the next column
def next_cell(event, master, column, row):
    try:
        master.cells[column][row].focus_set()
        print(master.cells[column][row])
    except:
        print("Out of range")
    return "break"


# Copy function bound to Ctrl+c keys
def custom_copy(event):
    try:
        widget = event.widget
        text = widget.selection_get()
        widget.clipboard_clear()
        widget.clipboard_append(text)
        print("Copied:", text)

    except Exception as e:
        print("Copy error:", e)
    return "break"


# Paste function bound to Ctrl+v keys
def custom_paste(event):
    try:
        widget = event.widget
        text = widget.clipboard_get()
        widget.insert("insert", text)
        print("Pasted:", text)
    except Exception as e:
        print("Paste error:", e)
    return "break"


# Paste function to rows and cells
def paste_data_to_cells(event, master, col, row):
    widget = event.widget
    data_grid = widget.clipboard_get().strip().split("\n")
    for r_offset, line in enumerate(data_grid):
        if "\t" in line:
            cells = line.split("\t")
        elif "produkt" in line:
            cells = line.split(" ", 1)
        else:
            cells = line.split(":")
        for c_offset, cell_text in enumerate(cells):
            try:
                col_letter = auc[col + c_offset]
                target_cell = master.cells[col_letter][row + r_offset]
                target_cell.delete("0.0", "end")
                target_cell.insert("0.0", cell_text)
            except (KeyError, IndexError):
                print(f"Mimo pole: {col_letter} {row + r_offset}")
    return "break"


# Funkce, která bude volat další formátovací funkce (kontrola sloupců, načtení dat, redukce velikosti, zapsání do labelů)
def format_handler(master, submaster):
    checkboxes = master.checkboxes
    checked_checkboxes = []
    for checkbox, i in enumerate(checkboxes):
        col_letter = auc[checkbox]
        ischecked = checkboxes[col_letter].get()
        if ischecked == 1:
            checked_checkboxes.append(col_letter)
    print(checked_checkboxes)
    f.format_master(checked_checkboxes, master, submaster)
    return "break"


def res_format_handler(master, submaster):
    rows_to_fromat = config["Rezervace"]["fromat_rows"]
