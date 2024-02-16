#!/usr/bin/python3
"""
This script will add all arguments to a Python list
and save them to a file using JSON rep
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


json_filename = "add_item.json"
try:
    my_list = load_from_json_file(json_filename)
except Exception:
    my_list = []
my_list.extend(sys.argv[1:])
save_to_json_file(my_list, json_filename)
