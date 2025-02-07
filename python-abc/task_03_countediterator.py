#!/usr/bin/python3
"""
CountedIterator - Keeping Track of Iteration
"""


class CountedIterator:
    def __init__(self, iterable):
        """
        Initialize the iterator from the given iterable
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Get the next item from the iterator
        """
        # Increment the count
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """
        Return the current count
        """
        return self.count
