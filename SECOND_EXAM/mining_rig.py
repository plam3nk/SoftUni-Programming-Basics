from math import ceil

videocard_price = int(input())
transition_price = int(input())
electricity_per_day_videocard = float(input())
daily_profit_per_videocard = float(input())

price_videocards = videocard_price * 13
price_transitions = transition_price * 13
total_spent = price_videocards + price_transitions + 1000

daily_profit_videocard = daily_profit_per_videocard - electricity_per_day_videocard
daily_profit = daily_profit_videocard * 13
backup_days = total_spent / daily_profit
print(total_spent)
print(ceil(backup_days))
