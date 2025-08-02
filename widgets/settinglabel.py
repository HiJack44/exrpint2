#Labels class for settings menu. Labels need to be at the same line as options

import customtkinter as ctik

class MenuItem(ctik.CTkLabel):
    def __init__(self, master, text, *args, **kwargs):
        super().__init__(master, text = text, *args, **kwargs)

        self.text = text
        self.configure(corner_radius=0)
        self.configure(fg_color='transparent')