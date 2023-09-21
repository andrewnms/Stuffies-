import random

while True:
    lvl = input("Level: ")
    if lvl.isdigit():
        if int(lvl) > 0:
            break

actualnum = random.randint(1, int(lvl))

while True:
    while True:
        guess = input("Guess: ")
        if guess.isdigit():
            if int(guess) > 0:
                break
    if int(guess) > actualnum:
        print("Too large!")
    elif int(guess) < actualnum:
        print("Too small!")
    else:
        print("Just Right!")
        break
