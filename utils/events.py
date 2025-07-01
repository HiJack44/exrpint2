#Key-bound events
import pyperclip as pc
import clipboard
from constants import auc

#Focus the cell in the next column
def next_cell(event,master,column, row):
    try:
        master.cells[column][row].focus_set()
        print(master.cells[column][row])
    except:
        print("Out of range")
    return "break"

#Copy function bound to Ctrl+c keys
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

#Paste function bound to Ctrl+v keys
def custom_paste(event):
    try:
        widget = event.widget
        text = widget.clipboard_get()
        widget.insert("insert", text)
        print("Pasted:",text)
    except Exception as e:
        print("Paste error:", e)
    return "break"

def paste_to_dict(event):
    widget = event.widget
    data = widget.clipboard_get().strip().split("\t")
    widget.insert('0.0', data)
    print(data)

    return "break"
def paste_data_to_cells(event, master, col, row):
    widget = event.widget
    data = widget.clipboard_get().strip().split("\t")
    for cell in data:
        col_letter = auc[col]
        master.cells[col_letter][row].insert('0.0', cell)
        col += 1
    return "break"
