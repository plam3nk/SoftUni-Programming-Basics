budget = float(input())
amount_of_statist = int(input())
price_of_clothing_one_statist = float(input())

decor = budget * 0.10
if amount_of_statist > 150:
    price_of_clothing_one_statist = price_of_clothing_one_statist * 0.90

clothing = price_of_clothing_one_statist * amount_of_statist
final_sum = decor + clothing
need_left = budget - final_sum

if final_sum > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {abs(need_left):.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {need_left:.2f} leva left.")