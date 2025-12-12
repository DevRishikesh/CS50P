import sys
import requests

if len(sys.argv)<2:
    sys.exit(1)
    print("Missing command-line argument")

try:
    coin=float(sys.argv[1])

    url="https://api.coincap.io/v2/assets/bitcoin?apiKey=85603e04ebb5c5154febdded7eb8dc65f642cdeb77ee01bdf12b3b07a58ff18d"
    response=requests.get(url)
    data=response.json()
    price = float(data["data"]["priceUsd"])
    print(price)
    total_value = price * coin

    print(f"${total_value:,.4f}")
except ValueError:
    sys.exit(1)
    print("Command-line argument is not a number")


