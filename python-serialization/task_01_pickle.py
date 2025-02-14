#!/usr/bin/env python3
"""
Module for custom object serialization using pickle.
"""

import pickle


class CustomObject:

    """
    A custom class with serialization and deserialization capabilities.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize the CustomObject with name, age, and student status.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object and save it to a file.

        Args:
        filename (str): The name of the file to save the serialized object.

        Returns:
        None
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error serializing object: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"Error deserializing object: {e}")
            return None
