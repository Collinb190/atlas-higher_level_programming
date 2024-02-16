#!/usr/bin/python3
"""
Defines the print_sorted method and MyList class
"""


class MyList(list):
    """This class inherits from the list class"""
    def print_sorted(self):
        """This prints a sorted list in ascening order"""
        print(sorted(self))
