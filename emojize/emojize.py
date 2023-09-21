# This code takes a string as input and returns a modified string with emojis in place of certain words. The code uses the emoji library to do this. The code could be used in a chatbot or other program that needs to convert text to emoji.
from emoji import emojize


def emojitranslate(text):
    return emojize(text, language="alias")


def main():
    message = emojitranslate(input("Input: "))
    print("Output:", message)


if __name__ == "__main__":
    main()
