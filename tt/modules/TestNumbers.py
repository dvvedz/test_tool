import random

class TestNumbers:
    def randNumb(self, len):
        return "".join(str( random.randint(0, 9) ) for i in range( len ))