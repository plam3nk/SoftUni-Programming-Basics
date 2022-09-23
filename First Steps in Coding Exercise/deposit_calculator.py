deposit_amount = float(input())
months_of_deposit = int(input())
year_percent = float(input())

increase_per_month = (deposit_amount * year_percent / 100) / 12
sum = deposit_amount + months_of_deposit * increase_per_month

print(sum)

