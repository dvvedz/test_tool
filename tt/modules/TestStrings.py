import string 
import random
from urllib import parse
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
    
    def randSpecChar(self, len):
        specChars = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~" + '"'
        return "".join(random.choice(list(specChars)) for i in range( len ))

    def urlEncode(self, stri):
        return parse.quote(stri)

    def urlDecode(self, stri):
        return parse.unquote(stri)