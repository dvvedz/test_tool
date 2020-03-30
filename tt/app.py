import sys
import argparse

from modules.TestStrings import TestStrings
from modules.TestNumbers import TestNumbers

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
        
    
