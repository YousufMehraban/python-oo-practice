"""Python serial number generator."""

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
        """initialize a new generator, starting serial is start """
        self.start = start
        self.begin = start
    def generate(self):
        """generate consequent serial numbers, starting at start"""
        self.start +=1
        return self.start - 1

    def reset(self):
        """reset the start to its initial value"""
        self.start = self.begin

    def __repr__(self):
        """print the object representation"""
        return f'<SerialGenerator start={self.begin} next={self.start}>'
