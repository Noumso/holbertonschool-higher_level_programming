#!/usr/bin/python3
"""define class"""


def is_kind_of_class(obj, a_class):
    """kind of class return True if is an instance
    or the object is an instance of a class that inherited from
    """
    return isinstance(obj, a_class)
