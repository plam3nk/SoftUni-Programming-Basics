kilometres = int(input())
day_or_night = input()

if kilometres < 20:
    start_price = 0.70
    if day_or_night == "day":
        price_per_km = 0.79
        total = kilometres * price_per_km + start_price
    elif day_or_night == "night":
        price_per_km = 0.9
        total = kilometres * price_per_km + start_price
elif kilometres < 100:
    price_per_km = 0.09
    total = kilometres * price_per_km
else:
    price_per_km = 0.06
    total = kilometres * price_per_km
print(f"{total:.2f}")