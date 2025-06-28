#Key-bound events
import pyperclip as pc

#Focus the cell in the next column
def next_cell(event,master,column, row):
    try:
        master.cells[column][row].focus_set()
        print(master.cells[column][row])
    except:
        print("Out of range")
    return "break"

def get_paste(event):
    try:
        text = pc.paste()
        print(text)
    except:
        print("An error occured")
    return "break"

def copy_some(event, copyii):
    text = copyii
    print(text)

    return "break"