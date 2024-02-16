#!/usr/bin/python3
"""This module will define the function text_indentation"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these chars: ., ? and :
    Args:
        text: the input text
    Raises:
        TypeError: if the input text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    separators = ['.', '?', ':']
    lines = []
    current = ""
    for char in text:
        current += char
        if char in separators:
            lines.append(current.strip())
            lines.append("")
            current = ""
    if current:
        lines.append(current.strip())
    print("\n".join(lines), end="")
