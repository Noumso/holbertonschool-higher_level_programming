#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.
    This class serves as a blueprint for all animal subclasses.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses
        """
        pass


class Dog(Animal):
    """
    subclass representing a dog
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    subclass representing a cat
    """

    def sound(self):
        return "Meow"
