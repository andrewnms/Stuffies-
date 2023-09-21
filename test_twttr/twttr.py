def main():
    x = shorten(input("Word: "))
    print(x)


def shorten(word):
    removed = ["a", "e", "i", "o", "u"]
    out = [word[0]]
    if out in removed:
        out.remove(out[0])
    for char in word[:]:
        if char.lower() not in removed:
            out += char
    return print("Output:", "".join(out))


if __name__ == "__main__":
    main()
