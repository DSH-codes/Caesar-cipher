
import customtkinter as ct
import string as st


def cleaner(widget: ct.CTkTextbox):
    """Deletes content of the Textbox widget"""

    widget.delete(0.0, ct.END)


def encode(message: str, shift = 1) -> str:
    """
    Encodes a message/string using the Caesar's
    cipher.

    Parameters:
        message(str): a string to be encoded
        shift(int): a shift of alphabet

    Returns:
        str: encoded message as a string value

    Examples:
        > encode("Hello", 3)

        > encode("London", 4)

        > encode("Hello world!", 2)
    """



    ab = [i for i in st.ascii_lowercase]  # stands for alphabet, content = lowercase english alphabet
    abu = [i for i in st.ascii_uppercase]  # the same as above but uppercase




    converted = [ab[ab.index(i) + shift] if i in ab and i != " " else i for i in message.lower()]
    converted = "".join(converted)

    return converted


print(encode("aaa!", 2))














