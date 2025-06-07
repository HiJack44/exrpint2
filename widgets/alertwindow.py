#This is class for alert windows
import customtkinter as ctik

class AlertWindow(ctik.CTkToplevel):
    def __init__(self, master, msg, *args, **kwargs):
        super().__init__(master, msg, *args, **kwargs)

