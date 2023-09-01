def main():
    MealT = convert(input("What time is it? "))
    if 7.00 <= MealT <= 8.00:
        print("breakfast time")
    elif 12.00 <= MealT <= 13.00:
        print("lunch time")
    elif 18.00 <= MealT <= 19.00:
        print("dinner time")


def convert(time):
    hours, minutes = time.strip().split(":")

    minutes = round(float(minutes) / 60, 2)
    time = float(hours) + minutes
    time = round(time, 2)
    return time


if __name__ == "__main__":
    main()
