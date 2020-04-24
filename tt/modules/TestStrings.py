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
        val = base64.b64encode(stri.encode())
        return val.decode("utf-8")
    
    def base64dec(self, stri):
        val =  base64.b64decode(stri)
        return val.decode("utf-8")
    
    def counterStri(self, leng):
        # TODO: fix so that the user can change separator char from "*" to what ever is inputed as an argument
        arr = []
        i = 2 

        while i < leng +1:
            try:
                iLen = len(str( i )) # Get current lenth of i
                iLenPrev = len(str(arr[-iLen]))
                iPrev = str(arr[-2])

                if iLen != iLenPrev:
                    i = int(iPrev) + iLen +1

            except IndexError: pass

            arr.append(i)
            arr.append("*")

            i += iLen +1

        csLen = "".join(str(c) for c in arr)

        if leng > len(csLen):
            arr.append(str(i)[:leng - len(csLen)])
            csLen = "".join(str(c) for c in arr)
        elif leng < len(csLen):
            csLen = csLen[:-(len(csLen) - leng)]

        return csLen
