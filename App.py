
import customtkinter as ui

import functions as fcs


# Giving the command value, to widgets, trough configure, is done for readability



class App(ui.CTk):
    button_padding_y = 10  # vertical
    button_padding_x = 15  # horizontal


    def __init__(self, geometry="400x600"):
        super().__init__()
        self.geometry(geometry)
        self.resizable(True, True)
        self.title(f"{' ' * 42}CaesarCipher 0.2")
        self.validation_ = (self.register(fcs.valid_digit), "%P")

        self.entry = ui.CTkEntry(self, validate = "key", validatecommand = self.validation_)
        self.entry.pack(pady=30)

        self.original_textbox = ui.CTkTextbox(self, width=350, height=180, corner_radius=15)
        self.original_textbox.pack(pady = 1)

        self.encoded_textbox = ui.CTkTextbox(self, width=350, height=180, corner_radius=15, state ="disabled")
        self.encoded_textbox.pack(pady = 1)

        self.frame_ = ui.CTkFrame(self, fg_color=self.cget("fg_color"), height=150, width=350)
        self.frame_.pack()

        self.import_ = ui.CTkButton(self.frame_, text="Import")
        self.import_.configure(command=lambda: fcs.insert_imported_text(self.original_textbox, fcs.import_text, fcs.clear, self.original_textbox, self.encoded_textbox))
        self.import_.grid(row=0, column=0, pady=self.button_padding_y, padx=self.button_padding_x)

        self.encode_ = ui.CTkButton(self.frame_, text="Encode")
        args = (self.original_textbox, self.entry, fcs.encoder, fcs.convert_lines, self.encoded_textbox)
        self.encode_.configure(command = lambda: fcs.show_secret(*args))
        self.encode_.grid(row=0, column=1, pady=self.button_padding_y, padx=self.button_padding_x)

        self.save_as = ui.CTkButton(self.frame_, text="Save as")
        self.save_as.grid(row=1, column=0, pady=self.button_padding_y, padx=self.button_padding_x)

        self.decode = ui.CTkButton(self.frame_, text="Decode")
        self.decode.grid(row=1, column=1, pady=self.button_padding_y, padx=self.button_padding_x)

        self.help = ui.CTkButton(self.frame_, text="Help", command = None)
        self.help.grid(row=2, column=0, pady=self.button_padding_y, padx=self.button_padding_x)

        self.clear_window = ui.CTkButton(self.frame_, text="Clear")
        self.clear_window.configure(command=self.clear_textboxes)
        self.clear_window.grid(row=2, column=1, pady=self.button_padding_y, padx=self.button_padding_x)

    def clear_textboxes(self):

        """Clears the two text boxes"""

        # Just clears the first textbox
        # Then do the same for the second one

        self.original_textbox.delete(0.0, "end")

        # Doing it this way, because ->
        # if widget["state"] = "disabled"
        # <- is not available

        self.encoded_textbox.configure(state = "normal")
        self.encoded_textbox.delete(0.0, "end")
        self.encoded_textbox.configure(state = "disabled")



if __name__ == "__main__":
    app = App()
    app.mainloop()
