def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    count = 0
    check = False

    if s[0:1].isalpha():
        check = True
    if check is True:
        for i in s:
            count += 1

        if 2 <= count <= 6:
            digit_found = None
            first_digit = True

            for i in s:
                if i.isdigit():
                    digit_found = True
                    if first_digit and i == "0":
                        check = False
                    first_digit = False

                if digit_found is not None and not i.isdigit():
                    check = False

                if (
                    33 <= ord(i) <= 47
                    or 58 <= ord(i) <= 64
                    or 91 <= ord(i) <= 96
                    or 123 <= ord(i) <= 126
                ):
                    check = False
        else:
            check = False
    return check


main()
