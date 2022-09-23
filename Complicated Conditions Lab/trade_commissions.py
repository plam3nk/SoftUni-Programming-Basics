town = input()
sales = float(input())

commissions = 0

if 0 <= sales <= 500:
    if town == "Sofia":
        commissions = 0.05
    elif town == "Varna":
        commissions = 0.045
    elif town == "Plovdiv":
        commissions = 0.055
elif 500 < sales <= 1000:
    if town == "Sofia":
        commissions = 0.07
    elif town == "Varna":
        commissions = 0.075
    elif town == "Plovdiv":
        commissions = 0.08
elif 1000 < sales <= 10000:
    if town == "Sofia":
        commissions = 0.08
    elif town == "Varna":
        commissions = 0.10
    elif town == "Plovdiv":
        commissions = 0.12
elif sales > 10000:
    if town == "Sofia":
        commissions = 0.12
    elif town == "Varna":
        commissions = 0.13
    elif town == "Plovdiv":
        commissions = 0.145
if commissions != 0:
    commissions = commissions * sales
    print(f"{commissions:.2f}")
else:
    print("error")