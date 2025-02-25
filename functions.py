
import customtkinter as ct

import string as st




def cleaner(widget: ct.CTkTextbox) -> None:
    """Deletes content of the Textbox widget

    Parameters:
        widget(CTk.Textbox)

    """

    widget.delete(0.0, ct.END)


def encode(message: str, shift = 1) -> str:
    """
    Encodes a message/string using the Caesar's
    cipher.

    Parameters:
        message(str): a string to be encoded
        shift(int): a shift of the alphabet

    Returns:
        converted(str): encoded message as a string value

    Examples:
        >>> encode("Hello", 3)
        'Khoor'
        >>> encode("London", 4)
        'Psrhsr'
        >>> encode("Hello world!", 2)
        'Jgnnq yqtnf!'
        >>> encode("I am 25 years old", 2)
        'K co 25 agctu qnf'

    """



    al = [i for i in st.ascii_lowercase]  # EN alphabet lowercase
    au = [i for i in st.ascii_uppercase]  # EN alphabet uppercase

    # the formula for encoding is: (alphabet.index(char) + shift) % len(alphabet)

    # The comprehension below is too complicated? This is because of this ternary -> (al if i.islower() else au) <-  marked by dashes
    # This version with no ternary, but works only with LOWERCASE messages: converted = [al[(al.index(i) + shift) % len(al)] if i in al and i != " " else i for i in message.lower()]
    # This version with no ternary, but works only with UPPERCASE messages: converted = [au[(au.index(i) + shift) % len(au)] if i in au and i != " " else i for i in message.lower()]


    #            --------------------------    -------------------------                                        -------------------------
    converted = [(al if i.islower() else au)[((al if i.islower() else au).index(i) + shift) % len(al)] if i in (al if i.islower() else au) and i != " " else i for i in message]
    converted = "".join(converted)

    return converted



