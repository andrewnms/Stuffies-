Expression = input("Expression: ").strip().split(" ")
x = float(Expression[0])
y = Expression[1]
z = float(Expression[2])
v = None

match y:
    case "+":
        v = x + z
        print(round(v, 1))
    case "-":
        v = x - z
        print(round(v, 1))
    case "*":
        v = x * z
        print(round(v, 1))
    case "/":
        if z != 0:
            v = x / z
            print(round(v, 1))
