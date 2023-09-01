def translate():
    while True:
        try:
            Fract = input("Fraction: ").split("/")
            if int(Fract[0]) > int(Fract[1]):
                continue
            else:
                perc = (int(Fract[0]) / int(Fract[1])) * 100
        except (ValueError, ZeroDivisionError):
            pass
        else:
            return perc


result = translate()
if isinstance(result, float):
    if result >= 99:
        print("F")
    elif result <= 1:
        print("E")
    else:
        print(f"{round(result)}%")
