items = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}
Total = 0
while True:
    try:
        order = input("Item: ")
    except EOFError:
        print("")
        break
    except KeyError:
        pass
    else:
        if order.title() in items:
            Total += items[order.title()]
            AbsTotal = format(Total, ".2f")
            print(f"${AbsTotal}")
