
import customtkinter as ct
import string as st


def cleaner(widget: ct.CTkTextbox):
    """Deletes content of the Textbox widget"""

    widget.delete(0.0, ct.END)


def encode(string, shift = 1):
    """Encodes a message/string using the Caesar's
    cipher

    Args:
        string: a string to be encoded
        shift: an integer to define the shift

    """

    alphabet = [i for i in st.ascii_lowercase]

    return "".join([alphabet[alphabet.index(i) + shift] if i != " " else i for i in string])


print(help(encode))








