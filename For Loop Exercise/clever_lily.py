age_lily = int(input())
price_washing_machine = float(input())
price_toy = int(input())

toys = 0
money = 0
get = 10

for n in range(1, age_lily + 1):
    if n % 2 == 0:
        money = money + get
        get = get + 10
        money = money - 1
    if n % 2 != 0:
        toys = toys + 1
money_from_toys = toys * price_toy
money = money + money_from_toys
diff = abs(money - price_washing_machine)
if money >= price_washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")