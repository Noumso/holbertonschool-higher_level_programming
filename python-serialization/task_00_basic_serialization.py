#!/usr/bin/python3
"""
Basic serialization module for Python dictionaries to JSON files and vice versa.
"""

import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file.

    Args:
    data (dict): The Python dictionary to be serialized.
    filename (str): The name of the file to save the JSON data.

    Returns:
    None
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file into a Python dictionary.

    Args:
    filename (str): The name of the file to load the JSON data from.

    Returns:
    dict: The deserialized Python dictionary.
    """
    with open(filename, 'r') as file:
        return json.load(file)
