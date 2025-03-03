# Docstrings ("""   """) :---


""" Dog Module

This module doews...bla bla bla and provides the following classes:

-Dog
...
"""


class Dog:
    """A class representing dog"""
    def __init__(self, name, age):
        """Initialize a new dog"""
        self.name = name
        self.age = age

        def bark(self):
            """let the dog bark"""
            print("WOF !")

    
print(help(Dog))
