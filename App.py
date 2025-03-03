
import customtkinter as ui

import functions





class App(ui.CTk):
    button_padding_y = 10  # vertical
    button_padding_x = 15  # horizontal

    def __init__(self, geometry="400x600"):
        super().__init__()
        self.geometry(geometry)
        self.resizable(True, True)
        self.title(f"{' ' * 42}CaesarCipher 0.2")

        self.entry = ui.CTkEntry(self)
        self.entry.pack(pady=30)

        self.original_text = ui.CTkTextbox(self, width=350, height=180, corner_radius=15)
        self.original_text.pack(pady = 1)

        self.encoded_text = ui.CTkTextbox(self, width=350, height=180, corner_radius=15, state = "disabled")
        self.encoded_text.pack(pady = 1)

        self.frame_ = ui.CTkFrame(self, fg_color=self.cget("fg_color"), height=150, width=350)
        self.frame_.pack()

        self.import_ = ui.CTkButton(self.frame_, text="Import")
        self.import_.grid(row=0, column=0, pady=self.button_padding_y, padx=self.button_padding_x)

        self.encode_ = ui.CTkButton(self.frame_, text="Encode", command = lambda: functions.encode_text(self.original_text, functions.encoding, self.encoded_text))
        self.encode_.grid(row=0, column=1, pady=self.button_padding_y, padx=self.button_padding_x)

        self.save_as = ui.CTkButton(self.frame_, text="Save as")
        self.save_as.grid(row=1, column=0, pady=self.button_padding_y, padx=self.button_padding_x)

        self.decode = ui.CTkButton(self.frame_, text="Decode")
        self.decode.grid(row=1, column=1, pady=self.button_padding_y, padx=self.button_padding_x)

        self.help = ui.CTkButton(self.frame_, text="Help")
        self.help.grid(row=2, column=0, pady=self.button_padding_y, padx=self.button_padding_x)

        self.clear_window = ui.CTkButton(self.frame_, text="Clear", command=lambda: functions.clean(self.original_text, self.encoded_text))
        self.clear_window.grid(row=2, column=1, pady=self.button_padding_y, padx=self.button_padding_x)



if __name__ == "__main__":
    app = App()
    app.mainloop()
