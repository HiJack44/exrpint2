import customtkinter as ctik

#class that defines individual cell
class Cell(ctik.CTkTextbox):
    def __init__(self, master, row, column, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.row = row
        self.column = column

    def __str__(self):
        return f"Hello, I am cell {self.column}{self.row}"

    def get_text(self):
        text = self.get('0.0', 'end')
        return "This is text" + text
