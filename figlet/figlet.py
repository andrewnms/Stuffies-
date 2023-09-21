import pyfiglet
import sys
import random


fontlist = pyfiglet.FigletFont.getFonts()
if len(sys.argv) < 2:
    msg = input("Input: ")
    translated = pyfiglet.figlet_format(msg, font=(random.choice(fontlist)))
    print(translated)
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] not in fontlist:
            sys.exit("Invalid usage")
        msg = input("Input: ")
        translated = pyfiglet.figlet_format(msg, font=(sys.argv[2]))
        print(translated)
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
