import customtkinter as ctik


# This will be a template for individual sticker representation in control window
class Sticker(ctik.CTkLabel):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, fg_color="pink", *args, **kwargs)
