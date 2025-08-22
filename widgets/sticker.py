import customtkinter as ctik
from config import config


# This will be a template for individual sticker representation in control window
class Sticker(ctik.CTkLabel):
    def __init__(self, master, text, *args, **kwargs):
        super().__init__(
            master,
            text=text,
            width=config["Sticker"]["width"],
            fg_color="#AAAAAA",
            *args,
            **kwargs
        )
        self.text = text

    # Function to obtain text from a sticker

    def get_label_text(self):
        return self.text
