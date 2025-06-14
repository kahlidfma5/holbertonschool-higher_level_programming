#!/usr/bin/python3
"""
Module that adds all arguments to a Python list, and then saves them to a file.
"""

import sys
import os.path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

my_list = []

if os.path.exists("add_item.json"):
    my_list = load_from_json_file("add_item.json")

my_list.extend(sys.argv[1:])

save_to_json_file(my_list, "add_item.json")
