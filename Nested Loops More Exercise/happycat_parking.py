days = int(input())
hours_per_day = int(input())

tax = 0
total = 0
for day in range(1, days + 1):
    daily_sum = 0
    for hour in range(1, hours_per_day + 1):
        if day % 2 == 0 and hour % 2 != 0:
            tax = 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            tax = 1.25
        else:
            tax = 1
        daily_sum += tax
    print(f"Day: {day} - {daily_sum:.2f} leva")
    total += daily_sum
print(f"Total: {total:.2f} leva")