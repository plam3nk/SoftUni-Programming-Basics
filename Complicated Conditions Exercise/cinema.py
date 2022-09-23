type_of_project = input()
rows = int(input())
columns = int(input())

all_seats = rows * columns
price = 0
if type_of_project == "Premiere":
    price = 12
elif type_of_project == "Normal":
    price = 7.50
elif type_of_project == "Discount":
    price = 5
income = all_seats * price
print(f"{income:.2f} leva")

