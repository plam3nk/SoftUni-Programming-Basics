type_of_fuel = input()
fuel_in_tank = float(input())

if fuel_in_tank < 25:
    if type_of_fuel == "Diesel":
        print(f"Fill your tank with diesel!")
    elif type_of_fuel == "Gasoline":
        print(f"Fill your tank with gasoline!")
    elif type_of_fuel == "Gas":
        print(f"Fill your tank with gas!")
    else:
        print(f"Invalid fuel!")
else:
    if type_of_fuel == "Diesel":
        print(f"You have enough diesel.")
    elif type_of_fuel == "Gasoline":
        print(f"You have enough gasoline.")
    elif type_of_fuel == "Gas":
        print(f"You have enough gas.")
    else:
        print(f"Invalid fuel!")