due = 50
coin = 0
while True:
    while due > 0:
        print(f"Amount Due: {due}")
        break
    while True:
        Usercoin = int(input("Insert Coin: "))
        match Usercoin:
            case 25:
                coin = Usercoin
                due -= coin
                coin = 0
                break
            case 10:
                coin = Usercoin
                due -= coin
                coin = 0
                break
            case 5:
                coin = Usercoin
                due -= coin
                coin = 0
                break
            case _:
                print(f"Amount Due: {due}")
                break
    if due < 0 and coin > due:
        print("Change Owed:", due * -1)
        break
    elif due == 0 and coin == 0:
        print("Change Owed: 0")
        break
