Greet = input("Greeting: ").lower().strip()
Value = 0
if Greet.startswith("h") and "hello" in Greet:
    print(f"${Value}")
elif Greet.startswith("h"):
    Value = 20
    print(f"${Value}")
else:
    Value = 100
    print(f"${Value}")
