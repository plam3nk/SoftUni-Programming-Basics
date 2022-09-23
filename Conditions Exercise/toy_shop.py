price_of_vacation = float(input())
puzzels = int(input())
talking_dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

amount_of_orders = puzzels + talking_dolls + bears + minions + trucks
price_puzzels = puzzels * 2.60
price_dolls = talking_dolls * 3
price_bears = bears * 4.10
price_minions = minions * 8.20
price_trucks = trucks * 2
total_sum = price_puzzels + price_dolls + price_bears + price_minions + price_trucks
discount = 0
total_sum_discount = 0
if amount_of_orders >= 50:
    discount = 0.25
    total_sum_discount = total_sum - total_sum * 0.25
else:
    total_sum_discount = total_sum
result = total_sum_discount - total_sum_discount * 0.10

if result >= price_of_vacation:
    money_left = result - price_of_vacation
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_left = result - price_of_vacation
    print(f"Not enough money! {abs(money_left):.2f} lv needed.")



