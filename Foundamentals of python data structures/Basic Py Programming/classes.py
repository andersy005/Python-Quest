
class Counter(object):
    """Models a counter"""

    # class variable
    instances = 0

    # constructor
    def __init__(self):
        """Sets up the counter"""
        Counter.instances += 1
        self.reset()

    # Mutator methods
    def reset(self):
        """sets the counter to 0"""
        self._value = 0

    def increment(self, amount=1):
        self._value += amount

    def decrement(self, amount=1):
        self._value -= amount

    # Accessor methods
    def getValue(self):
        return self._value

    def __str__(self):
        return str(self._value)

    def __eq__(self, other):
        if self is other:
            return True

        if type(self) != type(other):
            return False

        return self._value == other.value
