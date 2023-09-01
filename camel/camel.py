Case = input("camelCase: ")
checkdex = [Case[0]]
for char in Case[1:]:
    if char.isupper():
        checkdex += "_" + char
    else:
        checkdex += char
rez = "".join(checkdex).lower()
print("snake_case:", rez)
