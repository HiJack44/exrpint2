# Spinbox to make iterating over cell amount user friendly
from typing import Callable, Union

import customtkinter as ctik

class Spinbox(ctik.CTkFrame):
    def __init__(self,
                 *args,
                 width: int = 100,
                 height: int = 100,
                 value: Union[int] = 10,
                 command: Callable = None,
                 step_size: Union[int] = 1,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.command = command
        self.step_size = step_size

        self.configure(fg_color='lightgrey')

        self.grid_columnconfigure((0,2), weight=1)

        # Label that displays current number. Get method takes input from this label
        self.entry = ctik.CTkLabel(self, width=30, fg_color='lightgrey', text=value)
        self.entry.grid(row=0, column=1, padx=0, pady=0)

        # Substract button substracts number
        self.substract_button = ctik.CTkButton(self, width=15, text='-', command= lambda master=self:Spinbox.substract_number(master))
        self.substract_button.grid(row=0, column=0, padx=0, pady=0)

        # Add button adds number
        self.add_button = ctik.CTkButton(self, width=15, text='+', command= lambda master=self: Spinbox.add_number(master))
        self.add_button.grid(row=0, column=2, padx=0, pady=0, sticky='e')

    def get(self):
        return self.entry.cget("text")

    def substract_number(self):
        new_value = self.entry.cget("text") - self.step_size
        self.entry.configure(text=new_value)

    def add_number(self):
        new_value = self.entry.cget("text") + self.step_size
        self.entry.configure(text=new_value)
