#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    Writes the specified text to a file and returns
    the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        charsWritten = myFile.write(text)
    return (charsWritten)
