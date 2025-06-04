#frame for cells

import customtkinter as ctik
import cell

class Cellframe(ctik.CTkScrollableFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
