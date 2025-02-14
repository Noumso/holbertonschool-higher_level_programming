#!/usr/bin/env python3
"""
Module for converting CSV data to JSON format.
"""

import csv
import json


def convert_csv_to_json(csv_filename):

    """
    Converts data from a CSV file to JSON format and saves it to 'data.json'.

    Args:
    csv_filename (str): The name of the CSV file to convert.

    Returns:
    bool: True if conversion was successful, False otherwise.
    """
    try:

        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
