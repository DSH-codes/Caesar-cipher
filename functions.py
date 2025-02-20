
import customtkinter as ct


def cleaner(widget: ct.CTkTextbox):
    """Deletes content of the Textbox widget"""

    widget.delete(0.0, ct.END)


def encode():
    """Encodes text messages
    """
    ...
