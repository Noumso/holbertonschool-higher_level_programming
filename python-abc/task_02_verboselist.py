#!/usr/bin/python3

"""
Extending the Python List with Notifications
"""


class VerboseList(list):
    """
    List that provides notifications when elements are added or removed.
    """

    def append(self, element):
        """
        Adds an element to the list
        """
        super().append(element)
        print(f"Added [{element}] to the list.")

    def extend(self, elements):
        """
        Extends the list with multiple elements
        """
        count = len(elements)
        super().extend(elements)
        print(f"Extended the list with [{count}] items.")

    def remove(self, element):
        """
        Removes an element from the list
        """
        print(f"Removed [{element}] from the list.")
        super().remove(element)

    def pop(self, index=-1):
        """
        Removes and returns an element from the list
        """
        element = self[index]
        print(f"Popped [{element}] from the list.")
        return super().pop(index)
