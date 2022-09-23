type_of_flowers = input()
amount_flowers = int(input())
budget = int(input())

price = 0

if type_of_flowers == "Roses":
    price = 5
    if amount_flowers > 80:
        price= price * amount_flowers * 0.90
    else:
        price = price * amount_flowers
elif type_of_flowers == "Dahlias":
    price = 3.80
    if amount_flowers > 90:
        price = price * amount_flowers * 0.85
    else:
        price = price * amount_flowers
elif type_of_flowers == "Tulips":
    price = 2.80
    if amount_flowers > 80:
        price = price * amount_flowers * 0.85
    else:
        price = price * amount_flowers
elif type_of_flowers == "Narcissus":
    price = 3.00
    if amount_flowers < 120:
        price = (price * 1.15) * amount_flowers
    else:
        price = price * amount_flowers
elif type_of_flowers == "Gladiolus":
    price = 2.50
    if amount_flowers < 80:
        price = (price * 1.20) * amount_flowers
    else:
        price = price * amount_flowers
diff = abs(budget - price)

if budget >= price:
    print(f"Hey, you have a great garden with {amount_flowers} {type_of_flowers} and {diff:.2f} leva left.")
else:
    print (f"Not enough money, you need {diff:.2f} leva more.")


