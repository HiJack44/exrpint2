import customtkinter as ctik

class App(ctik.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x600")
        self.title("Exprint 2")



app = App()
app.mainloop()
