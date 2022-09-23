clients = int(input())
season = input()

price = 0
if season == "spring":
    price = 50
    if clients > 5:
        price = 48
elif season == "summer":
    price = 48.50
    if clients > 5:
        price = 45
elif season == "autumn":
    price = 60
    if clients > 5:
        price = 49.50
elif season == "winter":
    price = 86
    if clients > 5:
        price = 85
total = clients * price
if season == "summer":
    total = total * 0.85
elif season == "winter":
    total = total * 1.08
print(f"{total:.2f} leva.")