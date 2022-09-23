food_in_kg = int(input())
food_in_grams = food_in_kg * 1000
total_eaten = 0
command = input()
while command != "Adopted":
    grams_per_meal = int(command)
    total_eaten += grams_per_meal
    command = input()

diff = abs(food_in_grams - total_eaten)
if food_in_grams >= total_eaten:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")
