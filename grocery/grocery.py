Groceries = []
counter = {}

# Grabs the items to put inside the grocery list
while True:
    try:
        item = input().lower()
        Groceries.append(item)
    except EOFError:
        break
    except KeyError:
        pass


# Check's amount of times something is in the list
for food in Groceries:
    if food in counter:
        counter[food] += 1
    else:
        counter[food] = 1

# Shows the output
for food, value in sorted(counter.items()):
    print(f"{value} {food.upper()}")
