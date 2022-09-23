from math import ceil, floor

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cactuses = int(input())
gift_price = float(input())

magnolias_price = magnolias * 3.25
hyacinths_price = hyacinths * 4
roses_price = roses * 3.5
cactuses_price = cactuses * 8
total = magnolias_price + hyacinths_price + roses_price + cactuses_price
profit = total * 0.95
diff = abs(gift_price - profit)

if profit >= gift_price:
    print(f"She is left with {floor(diff)} leva.")
else:
    print(f"She will have to borrow {ceil(diff)} leva.")