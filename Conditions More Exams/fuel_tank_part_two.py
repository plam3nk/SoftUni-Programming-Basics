type_of_fuel = input()
fuel = float(input())
club_cart = input()

if type_of_fuel == "Gas":
    if club_cart == "Yes":
        price_per_liter = 0.93 - 0.08
        if 20 < fuel <= 25:
            total = price_per_liter * fuel * 0.92
        elif fuel > 25:
            total = price_per_liter * fuel * 0.90
        else:
            total = price_per_liter * fuel

    elif club_cart == "No":
        price_per_liter = 0.93
        if 20 < fuel <= 25:
            total = price_per_liter * fuel * 0.92
        elif fuel > 25:
            total = price_per_liter * fuel * 0.90
        else:
            total = price_per_liter * fuel

if type_of_fuel == "Gasoline":
    if club_cart == "Yes":
        price_per_liter = 2.22 - 0.18
        if 20 < fuel <= 25:
            total = price_per_liter * fuel * 0.92
        elif fuel > 25:
            total = price_per_liter * fuel * 0.90
        else:
            total = price_per_liter * fuel

    elif club_cart == "No":
        price_per_liter = 2.22
        if 20 < fuel <= 25:
            total = price_per_liter * fuel * 0.92
        elif fuel > 25:
            total = price_per_liter * fuel * 0.90
        else:
            total = price_per_liter * fuel

if type_of_fuel == "Diesel":
    if club_cart == "Yes":
        price_per_liter = 2.33 - 0.12
        if 20 < fuel <= 25:
            total = price_per_liter * fuel * 0.92
        elif fuel > 25:
            total = price_per_liter * fuel * 0.90
        else:
            total = price_per_liter * fuel

    elif club_cart == "No":
        price_per_liter = 2.33
        if 20 < fuel <= 25:
            total = price_per_liter * fuel * 0.92
        elif fuel > 25:
            total = price_per_liter * fuel * 0.90
        else:
            total = price_per_liter * fuel
print(f"{total:.2f} lv.")
