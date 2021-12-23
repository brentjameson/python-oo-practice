"""Python serial number generator."""

import math

class SerialGenerator:
    counter = 0
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

    def __init__(self, start):
        self.start = start
    
    def reset(self):
        print('doooough')
        self.start = self.start - self.counter
        return f"The serial number has been reset to it's original start number of {self.start}"

    def generate(self):
        self.start += 1
        self.counter += 1
        return self.start
        # math.nextafter(self.start,math.inf)
        