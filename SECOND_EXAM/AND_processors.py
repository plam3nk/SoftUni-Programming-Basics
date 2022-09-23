from math import floor

needed_processors = int(input())
workers = int(input())
days_working = int(input())

total_hours = workers * 8 * days_working
made_processors = total_hours / 3
diff = abs(needed_processors - floor(made_processors))
money_diff = diff * 110.10
if made_processors >= needed_processors:
    print(f"Profit: -> {money_diff:.2f} BGN")
else:
    print(f"Losses: -> {money_diff:.2f} BGN")