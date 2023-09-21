import requests
import sys

r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")


def check_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


current_price = r.json()["bpi"]["USD"]["rate_float"]
asked_price = float(sys.argv[1]) * float(current_price)


try:
    if check_float(sys.argv[1]):
        print(f"${asked_price:,}")
    else:
        sys.exit()
except requests.RequestException:
    sys.exit()
except IndexError:
    print("Missing command-line argument")
    sys.exit()
