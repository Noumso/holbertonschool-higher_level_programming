#!/usr/bin/python3
"""
The Enigmatic FlyingFish - Exploring Multiple Inheritance 
"""


class Fish:
    def swim(self):
        """
        Print a message indicating the fish is swimming
        """
        print("The fish is swimming")
    
    def habitat(self):
        """
        Print a message indicating the fish lives in water
        """
        print("The fish lives in water")

class Bird:
    def fly(self):
        """
        Print a message indicating the bird is flying
        """
        print("The bird is flying")
    
    def habitat(self):
        """
        Print a message indicating the bird lives in the sky
        """
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    def fly(self):
        """
        Print a message indicating the flying fish is soaring
        """
        print("The flying fish is soaring!")
    
    def swim(self):
        """
        Print a message indicating the flying fish is swimming
        """
        print("The flying fish is swimming!")
    
    def habitat(self):
        """
        Print a message indicating the flying fish lives both in water and the sky
        """
        print("The flying fish lives both in water and the sky!")
