"""Python serial number generator."""
from typing import List

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

def __init__(self, start=0):
    """Create a new serial number generator with a starting number."""
    self.start = self.next = start

def __repr__(self):
    return f"<SerialGenerator start={self.start} next={self.next}>"

def generate(self):
    """Return the next serial number."""
    self.next += 1
    return self.next - 1

def reset(self):
    """Reset the serial number to the original start number."""
    self.next = self.start