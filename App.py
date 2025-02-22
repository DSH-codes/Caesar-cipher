
import customtkinter as ui

import string as st

import functions

# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


class App(ui.CTk):

    button_padding_y = 10    # vertical
    button_padding_x = 15    # horizontal

    def __init__(self, geometry = "400x600"):

        super().__init__()
        self.geometry(geometry)
        self.resizable(True, True)
        self.title(f"{' ' * 42}CaesarCipher 0.2")

        self.entry = ui.CTkEntry(self)
        self.entry.pack(pady = 30)

        self.window = ui.CTkTextbox(self, width = 350, height = 350, corner_radius = 15)
        self.window.pack()

        self.frame_ = ui.CTkFrame(self, fg_color = self.cget("fg_color"), height = 150, width = 350)
        self.frame_.pack()

        self.import_ = ui.CTkButton(self.frame_, text = "Import")
        self.import_.grid(row = 0, column = 0, pady = self.button_padding_y, padx = self.button_padding_x)

        self.encode_ = ui.CTkButton(self.frame_, text = "Encode")
        self.encode_.grid(row = 0, column = 1, pady = self.button_padding_y, padx = self.button_padding_x)

        self.save_as = ui.CTkButton(self.frame_, text = "Save as")
        self.save_as.grid(row = 1, column = 0, pady = self.button_padding_y, padx = self.button_padding_x)

        self.decode = ui.CTkButton(self.frame_, text ="Decode")
        self.decode.grid(row = 1, column = 1, pady = self.button_padding_y, padx = self.button_padding_x)

        self.help = ui.CTkButton(self.frame_, text="Help")
        self.help.grid(row = 2, column = 0, pady=self.button_padding_y, padx=self.button_padding_x)

        self.clear_window = ui.CTkButton(self.frame_, text="Clear", command = lambda: functions.cleaner(self.window))
        self.clear_window.grid(row = 2, column = 1, pady = self.button_padding_y, padx=self.button_padding_x)







if __name__ == "__main__":

    app = App()
    app.mainloop()
