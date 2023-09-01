words = input("Input: ")
removed = ["a", "e", "i", "o", "u"]
out = [words[0]]
if out in removed:
    out.remove(out[0])
for char in words[1:]:
    if char.lower() not in removed:
        out += char
print("Output:", "".join(out))
