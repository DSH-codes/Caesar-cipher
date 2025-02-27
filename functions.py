
import customtkinter as ct

import string as st




def cleaner(*widgets: ct.CTkTextbox) -> None:
    """Deletes content of the Textbox widgets

    Parameters:
        widgets(CTk.Textbox)

    """
    for widget in widgets:
        widget.delete(0.0, "end")


def encoding(message: str, shift = 1) -> str:
    """
    Encodes a message/string using the Caesar's
    cipher.

    Parameters:
        message(str): a string to be encoded
        shift(int): a shift of the alphabet

    Returns:
        converted(str): encoded message as a string value

    Examples:
        >>> encoding("Hello", 3)
        'Khoor'
        >>> encoding("London", 4)
        'Psrhsr'
        >>> encoding("Hello world!", 2)
        'Jgnnq yqtnf!'
        >>> encoding("I am 25 years old", 2)
        'K co 25 agctu qnf'

    """



    al = [i for i in st.ascii_lowercase]  # EN alphabet lowercase
    au = [i for i in st.ascii_uppercase]  # EN alphabet uppercase

    # the formula for encoding is: (alphabet.index(char) + shift) % len(alphabet)

    # The comprehension below is too complicated? This is because of this ternary -> (al if i.islower() else au) <-  marked by dashes
    # This version with no ternary, but works only with LOWERCASE messages: converted = [al[(al.index(i) + shift) % len(al)] if i in al and i != " " else i for i in message.lower()]
    # This version with no ternary, but works only with UPPERCASE messages: converted = [au[(au.index(i) + shift) % len(au)] if i in au and i != " " else i for i in message.lower()]


    #            --------------------------    -------------------------                                        -------------------------
    converted = [(al if i.islower() else au)[((al if i.islower() else au).index(i) + shift) % len(al)] if i in (al if i.islower() else au) and i != " " and i != "\n" else i for i in message]
    converted = "".join(converted)

    return converted


def encode_text(widget: ct.CTkTextbox, encoder_, send = 0):

    text = widget.get(0.0, ct.END).split()
    #print(text)

    text = [encoder_(i) for i in text]

    # if send != 0:
    #     send.configure(state = "normal")
    #     send.insert(0.0, text)
    #     send.configure(state="disabled")


    print(text)
    #return text

