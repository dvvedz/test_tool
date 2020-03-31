import string 
import random
from urllib import parse
import base64

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

    def base46enc(self, stri):
        return base64.b64encode(stri.encode())
    
    def base64dec(self, stri):
        return base64.b64decode(stri.encode())