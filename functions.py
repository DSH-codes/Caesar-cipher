
import customtkinter as ct

import string as st

from typing import Callable, Union

from tkinter import filedialog as fd


# ---------------------------------------------WIDGETS OPERATING SECTION------------------------------------------------

def clear(*widgets: ct.CTkTextbox) -> None:
    """Deletes content of the Textbox widgets

    Parameters:
        widgets(CTk.Textbox): a Textbox widget
        to be cleared
    """

    # Just clears the first textbox
    # Then do the same for the second one

    widgets[0].delete(0.0, "end")

    # Doing it this way, because ->
    # if widget["state"] = "disabled"
    # <- is not available

    widgets[1].configure(state = "normal")
    widgets[1].delete(0.0, "end")
    widgets[1].configure(state = "disabled")


def show_secret(*args: Union[ct.CTkTextbox, ct.CTkEntry, Callable, Callable, ct.CTkTextbox]) -> None:
    """
    Takes a message from a textbox, encodes it
    and inserts it into another textbox

    Parameters:
        args[0]: a textbox widget to get a text from
        args[1]: an entry widget to get a shift from
        args[2]: a word encoding function to encrypt words using the given shift
        args[3]: a function to apply the word encoding func to every word in the text, and an give encrypted text
        args[4]: a textbox widget into which, encrypted text will be inserted


    What is going on here:

        This SHOW_SECRET function, takes a text from args[0] which is a Textbox widget.
        Then takes value from args[1] which an Entry widget and coverts it into int, it will be the shift value
        Then calls args[3] CONVERT_LINES function, passing to it args[2] ENCODER function along with the shift
        value and assigning the call to ENCRYPTED_MESSAGE variable
        Then ENCRYPTED_MESSAGE is inserted into args[4] which is a Textbox widget
    """

    shift = args[1].get()
    shift = int(shift) if shift else 1          # default is 1, if args[1].get() == " "

    encrypted_message = args[3](args[0], args[2], shift)

    target_widget = args[4]

    target_widget.configure(state = "normal")
    target_widget.delete(0.0, "end")            # delete the previous text, to avoid repetitive insertions
    target_widget.insert(0.0, encrypted_message)
    target_widget.configure(state = "disabled")


def insert_imported_text(to_where: ct.CTkTextbox, importing_function, clearing_function, *clear_them):

    clearing_function(*clear_them)

    text = importing_function()

    to_where.insert(0.0, text)


# ---------------------------------------------RETURNING FUNCTIONS SECTIONS---------------------------------------------


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




