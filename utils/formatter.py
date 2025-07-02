#this set of functions will format the text from cells and send them to the sticker labels
import pyperclip as pc
from constants import auc

def print_something():
    #text = main.app.tabview.cellfield1.get(cells)
    print("text")
    return "break"

def pritn_all_cells(arg):
    #from main import app
    text = arg.cellfield1.cells['A'][1].get_text()
    #text2 = pc.paste()
    print(text)

    return "break"

#Function to clear all the cells
def clear_cells(master):
    try:
        for col, i in enumerate(master.cells):
            col_letter = auc[col]
            for row, j in enumerate(master.cells[col_letter]):
                master.cells[col_letter][row].delete('0.0', 'end')
        print("All cells were erased")
    except:
        print("Erase failed")
    return "break"

