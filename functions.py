
import customtkinter as ct

import string as st

from typing import Callable, Union

from tkinter import filedialog as fd


# --------------------------------------------ONLY RETURNING FUNCTIONS HERE--------------------------------------------


def encoder(message: str, shift) -> str:
    """
    Encodes a message/string using the Caesar's
    cipher.

    Parameters:
        message(str): a string to be encoded
        shift(int): a shift of the alphabet

    Returns:
        converted(str): encoded message as a string value

    Examples:
        >>> encoder("Hello", 3)
        'Khoor'
        >>> encoder("London", 4)
        'Psrhsr'
        >>> encoder("Hello world!", 2)
        'Jgnnq yqtnf!'
        >>> encoder("I am 25 years old", 2)
        'K co 25 agctu qnf'

    """



    al = [i for i in st.ascii_lowercase]  # EN alphabet lowercase
    au = [i for i in st.ascii_uppercase]  # EN alphabet uppercase

    # the formula for encoding is: (alphabet.index(char) + shift) % len(alphabet)

    # The comprehension below is too complicated? This is because of this ternary -> (al if i.islower() else au) <-  marked by dashes
    # This version with no ternary, but works only with LOWERCASE messages: converted = [al[(al.index(i) + shift) % len(al)] if i in al and i != " " else i for i in message.lower()]
    # This version with no ternary, but works only with UPPERCASE messages: converted = [au[(au.index(i) + shift) % len(au)] if i in au and i != " " else i for i in message.lower()]


    #            --------------------------    -------------------------                                        -------------------------
    # converted = [(al if i.islower() else au)[((al if i.islower() else au).index(i) + shift) % len(al)] if i in (al if i.islower() else au) and i != " " and i != "\n" else i for i in message]
    converted = [(al if i.islower() else au)[((al if i.islower() else au).index(i) + shift) % len(al)] if i in (al if i.islower() else au) and i != " " else i for i in message]
    converted = "".join(converted)

    return converted


def convert_lines(from_widget: ct.CTkTextbox, encoding_function: Callable, shift_: int) -> str:
    """
    Takes a text from a widget, encodes it, by a
    given encoder function, and returns an encoded
    text

    Parameters:
        from_widget(str): a widget to get a text from
        encoding_function(function): a function to encode the text
        shift_(int): a value for shifting, to be given to encoding function

    Returns:
        text(str): the encoded text

    """


    text = from_widget.get(0.0, ct.END).splitlines(1)

    text = [encoding_function(i, shift_) for i in text]

    return "".join(text)


def valid_digit(x: str):

    """This function is for validation
    that only digits or empty string is
    in an entry

    Parameters:
        x(str): a value to be checked == %P
    """

    if x.isdigit() or x == "":
        return True
    return False


def import_text() -> str:
    """Gets a text file, to import
    some text from it.

    Returns:
        content(str): the extracted text
    """

    where = fd.askopenfilename()

    if not where:
        return

    with open(where, "r") as file:
        content = file.read()

    return content




