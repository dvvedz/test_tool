import string 
import random

class TestStrings:

    def randStrLow(self, len):
        letter = string.ascii_lowercase
        return "".join(random.choice( letter ) for i in range( len ))

    def randStrUpper(self, len):
        letter = string.ascii_uppercase
        return "".join(random.choice( letter ) for i in range( len ))

    def randStri(self, len):
        letter = string.ascii_letters
        return "".join(random.choice( letter ) for i in range( len ))