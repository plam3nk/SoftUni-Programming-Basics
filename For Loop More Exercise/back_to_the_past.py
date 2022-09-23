money = float(input())
year_he_will_live = int(input())
age = 18

for year in range(1800, year_he_will_live + 1):
    if year % 2 == 0:
        money -= 12000
    elif year % 2 != 0:
        money -= 12000 + 50 * age
    age += 1

if money >= 0:
    print(f"Yes! He will live a carefree life and will have {abs(money):.2f} dollars left.")
else:
    print(f"He will need {abs(money):.2f} dollars to survive.")

