#!/usr/bin/python3
"""
The Mystical Dragon - Mastering Mixins
"""


class SwimMixin:
    """
    Define the SwimMixin class with a swim method
    """
    def swim(self):
        """
        print the creature swim
        """
        print("The creature swims!")


class FlyMixin:
    """
    Define the FlyMixin class with a fly method
    """
    def fly(self):
        """
        print creature flies
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Define the Dragon class that inherits from SwimMixin and FlyMixin
    """
    def roar(self):
        """
        print dragon roars
        """
        print("The dragon roars!")
