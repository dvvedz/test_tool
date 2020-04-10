import sys
import argparse

from modules.TestStrings import TestStrings
from modules.TestNumbers import TestNumbers

if __name__ == "__main__":

    # init instances
    testStrings = TestStrings()
    randNum = TestNumbers()

    parser = argparse.ArgumentParser(description='Test tool')

    parser.add_argument("-rsl", type=int, help="Lowercase string")
    parser.add_argument("-rsu", type=int, help="Uppercase string")
    parser.add_argument("-rs", type=int, help="Upper and lowercase string")
    parser.add_argument("-rsr", type=int, help="Only special chars") # Needs fixing i think... more testing to be done
    parser.add_argument("-cs", type=int, help="Creates a counterstring")

    parser.add_argument("-ue", type=str, help="URL encode")
    parser.add_argument("-ud", type=str, help="URL decode")
    parser.add_argument("-be", type=str, help="Base64 encode")
    parser.add_argument("-bd", type=str, help="Base64 decode")

    parser.add_argument("-rn", type=int, help="Random numbers")

    args = parser.parse_args()
    # Strings
    if( args.rsl ): 
        val = testStrings.randStrLow( args.rsl )
    elif(args.rsu):
        val = testStrings.randStrUpper( args.rsu )
    elif(args.rs):
        val = testStrings.randStri( args.rs )
    elif ( args.rsr ):
        val = testStrings.randSpecChar( args.rsr )
    elif ( args.ue ):
        val = testStrings.urlEncode( args.ue )
    elif( args.ud ):
        val = testStrings.urlDecode( args.ud )
    elif( args.be ):
        val = testStrings.base46enc( args.be )
    elif( args.bd ):
        val = testStrings.base64dec( args.bd ) 
    elif( args.cs ): 
        val = testStrings.counterStri( args.cs )

    # Numbers    
    elif( args.rn ):
        val = randNum.randNumb( args.rn )

    try: 
        # Checks if arguments are supplied else prints a help 
        print(val)
    except NameError:
        parser.print_help()


