#this set of functions will format the text from cells and send them to the sticker labels
import pyperclip as pc

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

