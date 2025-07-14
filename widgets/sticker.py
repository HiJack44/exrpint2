import customtkinter as ctik
from config import config


# This will be a template for individual sticker representation in control window
class Sticker(ctik.CTkLabel):
    def __init__(self, master, *args, **kwargs):
        super().__init__(
            master, fg_color="pink", width=config["Sticker"]["width"], *args, **kwargs
        )
