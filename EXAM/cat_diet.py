percent_fat = int(input())
percent_protein = int(input())
percent_carbohydrate = int(input())
total_calories = int(input())
percent_water = int(input())

fat_grams = (percent_fat / 100 * total_calories) / 9
protein_grams = (percent_protein / 100 * total_calories) / 4
carbohydrate_grams = (percent_carbohydrate / 100 * total_calories) / 4
total_weight = fat_grams + protein_grams + carbohydrate_grams
calories_for_gram = total_calories / total_weight
only_food_percent = 100 - percent_water
calories_for_gram_without_water = only_food_percent / 100 * calories_for_gram
print(f"{calories_for_gram_without_water:.4f}")