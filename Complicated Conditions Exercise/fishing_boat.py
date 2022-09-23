group_budget = int(input())
season = input()
amount_fishers = int(input())

boat_price = 0

if season == "Spring":
    boat_price = 3000
    if amount_fishers <= 6:
        boat_price = boat_price * 0.90
    elif amount_fishers <= 11:
        boat_price = boat_price * 0.85
    else:
        boat_price = boat_price * 0.75
elif season == "Winter":
    boat_price = 2600
    if amount_fishers <= 6:
        boat_price = boat_price * 0.90
    elif amount_fishers <= 11:
        boat_price = boat_price * 0.85
    else:
        boat_price = boat_price * 0.75
elif season == "Summer" or season == "Autumn":
    boat_price = 4200
    if amount_fishers <= 6:
        boat_price = boat_price * 0.90
    elif amount_fishers <= 11:
        boat_price = boat_price * 0.85
    else:
        boat_price = boat_price * 0.75

if season == "Winter" or season == "Summer" or season ==  "Spring":
    if amount_fishers % 2 == 0:
        boat_price = boat_price * 0.95
diff = abs(group_budget - boat_price)

if group_budget >= boat_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")