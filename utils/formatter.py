#this set of functions will format the text from cells and send them to the sticker labels
#from main import app


def print_something():
    #text = main.app.tabview.cellfield1.get(cells)
    print("text")
    return "break"

def pritn_all_cells(arg):
    #from main import app
    text = arg.cells['A'][1].get_text()
    print(text)
    return "break"
