#This will be frame for stickers. It will display formated stickers

import customtkinter as ctik
import sticker as s

class Stickerframe(ctik.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        def stick_sticker(text, row):
            sticker = s.Sticker(self, text=text)
            sticker.grid(row=row, column=0)