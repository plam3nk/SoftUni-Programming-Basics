budget = float(input())
season = input()

destination = ''
cost = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        holiday = "Camp"
        cost = 0.30
    if season == "winter":
        holiday = "Hotel"
        cost = 0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        holiday = "Camp"
        cost = 0.40
    if season == "winter":
        holiday = "Hotel"
        cost = 0.80
else:
    destination = "Europe"
    holiday = "Hotel"
    cost = 0.90

spent_money = (budget * cost)
print(f"Somewhere in {destination}")
print(f"{holiday} - {spent_money:.2f}")

