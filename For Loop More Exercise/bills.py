months = int(input())
bills_electricity = 0
bills_water = 0
bills_internet = 0
bills_others = 0
bills_others_sum = 0
for month in range(1, months + 1):
    electricity = float(input())
    bills_electricity += electricity
    bills_water += 20
    bills_internet += 15
    bills_others = (electricity + 20 + 15) * 1.2
    bills_others_sum += bills_others

all_bills = bills_electricity + bills_water + bills_internet + bills_others_sum
average_bills_per_month = all_bills / months
print(f"Electricity: {bills_electricity:.2f} lv")
print(f"Water: {bills_water:.2f} lv")
print(f"Internet: {bills_internet:.2f} lv")
print(f"Other: {bills_others_sum:.2f} lv")
print(f"Average: {average_bills_per_month:.2f} lv")

