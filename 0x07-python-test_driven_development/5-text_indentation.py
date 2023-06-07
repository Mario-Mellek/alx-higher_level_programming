#!/usr/bin/python3
"""
The module contains a function
that prints a text with 2 new lines
after each of these characters:
".",
"?"
":".
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines
        after each of these characters: ".", "?", ":".

    Arguments:
        text (str): The text to be printed. Must be a string.

    Raises:
        TypeError: text must be a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    result = ''
    i = 0
    while i < len(text):
        if (text[i - 1] == ".") or\
         (text[i - 1] == "?") or (text[i - 1] == ":"):
            result += "\n" * 2
            if (text[i].isspace() is not True):
                result += text[i]
            i += 1
            continue
        result += text[i]
        i += 1
    print(result, end='')
