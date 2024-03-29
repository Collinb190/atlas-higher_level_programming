#!/usr/bin/python3
"""This module will define the base class."""
import json


class Base:
    """This will be the base of all other classes in this project."""
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """Constructor for each instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def get_nb_objects(cls):
        """Returns the private class attribute nb_objects"""
        return cls.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string rep of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        file_name = cls.__name__ + ".json"

        if list_objs is None:
            json_list = []
        else:
            json_list = [obj.to_dictionary() for obj in list_objs]

        with open(file_name, "w") as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string rep json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, "r") as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**dictionary) for dictionary in list_dicts]
        except FileNotFoundError:
            return []
