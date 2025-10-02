# This is class for alert windows
import customtkinter as ctik


class AlertWindow(ctik.CTkToplevel):
    def __init__(self, parent, title, msg,update_st: bool=False, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        """
        This is the general alert window. 
        It gets the parent module as a parametr and the info 
        if it's the update alert.
        It's a mess on windows so there are methods to keep it on top.  
        """

        self.geometry("200x300")
        self.title = title
        self.update_st = update_st
        self.attributes("-topmost", True)

        self.alert = ctik.CTkLabel(self, width=200, text=msg, wraplength=150)
        self.alert.pack(pady=10, padx=10)

        self.close_button = ctik.CTkButton(
            self, text="Zavřít", command=self.close_alert_window
        )
        self.close_button.pack(pady=5, padx=5)

        self.update_button = ctik.CTkButton(self, text="Aktualizovat", command=parent.update_app)

        if update_st == True:
            print("Update available")
            self.update_button.pack(pady=5, padx=5)


    def close_alert_window(self):
        self.destroy()


def open_alert(parent, title, msg, update_st: bool = False):
    if parent.alert_window is None or not parent.alert_window.winfo_exists():
        parent.alert_window = AlertWindow(parent, title, msg, update_st)
        parent.alert_window.focus_set()
    else:
        parent.alert_window.focus_set()

