#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            upChar = chr(ord(char) - ord('a') + ord('A'))
            result += "{}".format(upChar)
        else:
            result += "{}".format(char)
    result += '\n'
    print(result, end="")
