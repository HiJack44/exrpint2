# This will be frame for stickers. It will display formated stickers

import customtkinter as ctik


class Stickerframe(ctik.CTkScrollableFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
