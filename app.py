import random
import string 
import sys
import argparse

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

class TestNumbers:
    def randNumb(self, len):
        return "".join(str(random.randint(0, 9)) for i in range( len ))


if __name__ == "__main__":
    # init instances
    randStr = TestStrings()
    randNum = TestNumbers()

    parser = argparse.ArgumentParser(description='Test tool')

    parser.add_argument("-rsl", type=int, help="Lowercase random string")
    parser.add_argument("-rsu", type=int, help="Uppercase random string")
    parser.add_argument("-rs", type=int, help="Upper and lowercase random string")
    parser.add_argument("-rn", type=int, help="Random numbers")

    args = parser.parse_args()

    if( args.rsl ): 
        print(randStr.randStrLow( args.rsl ))
    elif(args.rsu):
        print(randStr.randStrUpper( args.rsu )) 
    elif(args.rs):
        print( randStr.randStri( args.rs ))
    elif( args.rn ):
        print( randNum.randNumb( args.rn ))
        
    
