# This is class for alert windows
import customtkinter as ctik


class AlertWindow(ctik.CTkToplevel):
    def __init__(self, master, msg, *args, **kwargs):
        super().__init__(master, msg, *args, **kwargs)

        self.geometry("200x300")

        self.alert = ctik.CTkLabel(self, width=200, text=msg, wraplength=150)
        self.alert.pack(pady=10, padx=10)

        self.close_button = ctik.CTkButton(self, text="Zavřít", command=self.close_alert_window)
        self.close_button.pack(pady=5, padx=5)

    def close_alert_window(self):
        pass
