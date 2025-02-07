#!/usr/bin/python3
"""define class"""


def inherits_from(obj, a_class):
    """ returns True if the object is
    an instance of a class that inherited or false
    """
    if type(obj) is a_class:
        return False
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
