import tkinter.messagebox

import customtkinter as ui

import functions as fcs

import webbrowser

import time as tm

from tkinter import filedialog as fd






# Giving the command value, to widgets, trough configure, is done for readability



class HelpWindow(ui.CTkToplevel):
    def __init__(self, lc_horizontal, lc_vertical):
        super().__init__()
        self.title("How to use")
        self.geometry(f"400x600+{lc_horizontal+400}+{lc_vertical}")
        # set the help window, right the next to the main window

        with open("how_to_use.txt") as file:
            instructions = file.read()

        self.frame = ui.CTkFrame(self)
        self.frame.pack(side = "top", pady = 10, fill = "x")

        self.info_label_ = ui.CTkTextbox(self.frame, height = 500, activate_scrollbars=False)
        self.info_label_.insert(0.0, instructions)
        self.info_label_.pack(side = "left", expand = True, fill = "x")
        self.info_label_.configure(state="disabled", font=("TimesNewRoman", 20), fg_color=['gray92', 'gray14'])

        self.go_to_wiki = ui.CTkButton(self, text = "Visit:en.wikipedia.org/wiki/Caesar_cipher")
        self.go_to_wiki.configure(command = self._visit_wiki)
        self.go_to_wiki.pack(pady = 20)

    def _visit_wiki(self):
        self.go_to_wiki.configure(fg_color = "limegreen")
        webbrowser.open("en.wikipedia.org/wiki/Caesar_cipher")



class App(ui.CTk):
    button_padding_y = 10  # vertical
    button_padding_x = 15  # horizontal
    font_size = 15

    def __init__(self):
        super().__init__()
        self.geometry("400x600")
        self.resizable(True, True)
        self.title(f"{' ' * 42}CaesarCipher 0.2")
        self.validation_ = (self.register(fcs.valid_digit), "%P")
        self.central_position()

        self.position_vertical = 0
        self.position_horizontal = 0

        self.entry = ui.CTkEntry(self, validate = "key", validatecommand = self.validation_)
        self.entry.pack(pady=30)

        self.original_textbox = ui.CTkTextbox(self, width=350, height=180, corner_radius=15)
        self.original_textbox.pack(pady = 1)

        self.encoded_textbox = ui.CTkTextbox(self, width=350, height=180, corner_radius=15, state ="disabled")
        self.encoded_textbox.pack(pady = 1)

        self.frame_ = ui.CTkFrame(self, fg_color=self.cget("fg_color"), height=150, width=350)
        self.frame_.pack()

        self.import_ = ui.CTkButton(self.frame_, text="Import")
        self.import_.configure(command=self._import_text)
        self.import_.grid(row=0, column=0, pady=self.button_padding_y, padx=self.button_padding_x)

        self.encode_ = ui.CTkButton(self.frame_, text="Encode")
        self.encode_.configure(command = self._encode_and_show)
        self.encode_.grid(row=0, column=1, pady=self.button_padding_y, padx=self.button_padding_x)

        self.save_as = ui.CTkButton(self.frame_, text="Save as")
        self.save_as.configure(command = self._save)
        self.save_as.grid(row=1, column=0, pady=self.button_padding_y, padx=self.button_padding_x)

        self.decode = ui.CTkButton(self.frame_, text="Decode")
        self.decode.grid(row=1, column=1, pady=self.button_padding_y, padx=self.button_padding_x)

        self.help = ui.CTkButton(self.frame_, text="Help", command = self._show_help)
        self.help.grid(row=2, column=0, pady=self.button_padding_y, padx=self.button_padding_x)

        self.clear_window = ui.CTkButton(self.frame_, text="Clear")
        self.clear_window.configure(command=self._clear_textboxes)
        self.clear_window.grid(row=2, column=1, pady=self.button_padding_y, padx=self.button_padding_x)

        self.help_window: None | ui.CTkToplevel = None

        # self.optimal_position()

    def _encode_and_show(self):
        """Gets a text from the upper textbox
        encodes it, the inserts into the textbox
        below"""

        shift = self.entry.get()
        shift = int(shift) if shift else 1

        encoded_message = fcs.convert_lines(self.original_textbox, fcs.encoder, shift)

        self._clear_textboxes(False)

        self.encoded_textbox.configure(state = "normal")
        self.encoded_textbox.insert(0.0, encoded_message)
        self.encoded_textbox.configure(state = "disabled")

    def _clear_textboxes(self, both = True):

        """Clears one or both
        of the textboxes"""

        # Just clears the first textbox
        # Then do the same for the second one

        self.encoded_textbox.configure(state="normal")
        self.encoded_textbox.delete(0.0, "end")
        self.encoded_textbox.configure(state="disabled")

        if not both:   # if not both, return
            return

        # Doing it this way, because ->
        # if widget["state"] = "disabled"
        # <- is not available

        self.original_textbox.delete(0.0, "end")

    def _import_text(self):
        """Takes a text from txt file
        and inserts it into the upper
        textbox for encoding"""

        text = fcs.import_text()

        if not text:
            return

        self._clear_textboxes()

        self.original_textbox.insert(0.0, text)

    def _save(self):
        """Saves original, encoded or
        both messages as a txt file."""

        original_message = self.original_textbox.get(0.0, "end")
        original_message = "no message was written\n" if original_message == "\n" else original_message

        # if no text in the textboxes, default values to be given

        encoded_message = self.encoded_textbox.get(0.0, "end")
        encoded_message = "no message was encoded" if encoded_message == "\n" else encoded_message

        file_name = "Secret Message " + str(tm.time()).replace(".", "")
        s = fd.asksaveasfilename(initialfile=file_name, defaultextension = ".txt", filetypes = [("Text file", "*.txt")])

        if not s:       # if filename was not taken, return
            return

        with open(s, "w") as file:
            file.write(original_message)
            file.write(f"\n{('-' * 45)}\n\n")
            file.write(encoded_message)

    def _show_help(self):

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        width = self.winfo_width()
        height = self.winfo_height()

        location_horizontal = (screen_width - width) // 2
        location_vertical = (screen_height - height) // 2


        if self.help_window is None or not self.help_window.winfo_exists():
            self.help_window = HelpWindow(location_horizontal, location_vertical)
            self.help_window.focus()
        else:
            self.help_window.focus()

    def central_position(self):
        """Calculates the main window's dimension and
        then places it precisely into the middle
        of the screen"""

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        width = self.winfo_width()
        height = self.winfo_height()

        location_horizontal = (screen_width - width) // 2
        location_vertical = (screen_height - height) // 2


        pos = f"{width}x{height}+{location_horizontal}+{location_vertical}"

        self.geometry(pos)




















if __name__ == "__main__":
    app = App()
    app.mainloop()
