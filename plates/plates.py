def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    count = 0
    check = False
    # check if the first character is a letter
    if s[0:1].isalpha():
        check = True
    # check if the length of the string is between 2 and 6
    if check is True:
        for i in s:
            count += 1

        if 2 <= count <= 6:
            # check if there is a digit in the string
            digit_found = None
            first_digit = True

            for i in s:
                if i.isdigit():
                    digit_found = True
                    # check if the first digit is 0
                    if first_digit and i == "0":
                        check = False
                    first_digit = False

                if digit_found is not None and not i.isdigit():
                    check = False
                # check if there is a special character in the string
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
