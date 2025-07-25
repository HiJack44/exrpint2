# This is class for alert windows
import customtkinter as ctik


class AlertWindow(ctik.CTkToplevel):
    def __init__(self, parent, title, msg, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.geometry("200x300")
        self.title = title

        self.alert = ctik.CTkLabel(self, width=200, text=msg, wraplength=150)
        self.alert.pack(pady=10, padx=10)

        self.close_button = ctik.CTkButton(self, text="Zavřít", command=self.close_alert_window)
        self.close_button.pack(pady=5, padx=5)

    def close_alert_window(self):
        self.destroy()

def open_alert(parent, title, msg):
    if parent.alert_window is None or not parent.alert_window.winfo_exists():
        parent.alert_window = AlertWindow(parent, title, msg)
    else:
        parent.alert_window.focus_set()