#Key-bound events


#Focus the cell in the next row
def next_row(event):
    print("Next row")
    event.widget.tk_focusNext().focus()
    return "break"

#Focus the cell in the next column
def next_cell(event,master,column, row):
    try:
        master.cells[column][row].focus_set()
        print(master.cells[column][row])
    except:
        print("Out of range")
    return "break"