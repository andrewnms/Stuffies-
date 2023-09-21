from twttr import shorten


def main():
    message = shorten(input("Word: "))
    print(message)


if __name__ == "__main__":
    main()
