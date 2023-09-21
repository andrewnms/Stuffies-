import inflect
import sys

p = inflect.engine()
names = []

while True:
    try:
        usermsg = input("Name: ")
        names.append(usermsg)
    except EOFError:
        if len(names) == 0:
            sys.exit()
        msg = p.join((names))
        print("")
        break

print(f"Adieu, adieu, to {msg}")
