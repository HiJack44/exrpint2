#Key-bound events
import pyperclip as pc
import clipboard

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