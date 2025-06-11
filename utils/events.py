#Key-bound events


#Focus the cell in the next column
def next_cell(event,master,column, row):
    try:
        master.cells[column][row].focus_set()
        print(master.cells[column][row])
    except:
        print("Out of range")
    return "break"