from math import floor, ceil

amount_of_days = int(input())
food_kg = int(input())
food_per_day_dog_kg = float(input())
food_per_day_cat_kg = float(input())
food_per_day_turtle_grams = float(input())

food_for_dog = amount_of_days * food_per_day_dog_kg
food_for_cat = amount_of_days * food_per_day_cat_kg
food_for_turtle = amount_of_days * food_per_day_turtle_grams / 1000
total_food = food_for_dog + food_for_cat + food_for_turtle
diff = abs(total_food - food_kg)

if total_food <= food_kg:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed.")