locations = int(input())
for location in range(locations):
    expected_gold_daily = float(input())
    days_mining = int(input())
    total_mined = 0
    for days in range(days_mining):
        mined_gold = float(input())
        total_mined += mined_gold
    average_mined = total_mined / days_mining
    diff = expected_gold_daily - average_mined
    if average_mined >= expected_gold_daily:
        print(f"Good job! Average gold per day: {average_mined:.2f}.")
    else:
        print(f"You need {diff:.2f} gold.")