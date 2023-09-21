import random


# This code is a game that tests the user's addition ability. The game requires the user to enter the correct answer to a series of addition problems. The user can choose the difficulty level of the problem. The user can also choose to skip a problem if they are stuck. The user is given a score at the end of the game.

# This code is a simple math quiz program
# It will ask 10 questions that are either addition or subtraction
# Questions will get harder as you progress through the quiz

import random


def main():
    # Initialize the counters
    answer_count = 0
    score = 0

    # Get the level
    level = get_level()

    # Ask 10 questions
    for _ in range(1, 10):
        # Generate two random numbers
        integers = generate_integer(level)
        first = integers[0]
        second = integers[1]

        # Ask the question
        ans = first + second
        while True:
            guess = input("{} + {} = ".format(first, second))
            if guess == str(ans):
                score += 1
                break
            else:
                print("EEE")
                answer_count += 1
            if answer_count == 3:
                print(f"{first} + {second} = {ans}")
                break
    print(f"Score:{score}")


def get_level():
    while True:
        level = input("Enter level: ")
        if level in ["1", "2", "3"]:
            return int(level)
        else:
            pass


def generate_integer(level):
    problem = []
    if level == 1:
        problem.append(random.randint(0, 9))
        problem.append(random.randint(0, 9))
    elif level == 2:
        problem.append(random.randint(10, 99))
        problem.append(random.randint(10, 99))
    elif level == 3:
        problem.append(random.randint(100, 999))
        problem.append(random.randint(100, 999))
    return problem


if __name__ == "__main__":
    main()
