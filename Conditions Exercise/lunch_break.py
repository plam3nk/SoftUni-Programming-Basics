from math import ceil

serial_name = input()
episode_time = int(input())
rest_lunch_time = int(input())

lunch_time = rest_lunch_time * 0.125
rest_time = rest_lunch_time * 0.25

all_time = rest_lunch_time - lunch_time - rest_time
diff = abs(episode_time - all_time)

if episode_time <= all_time:
    print(f"You have enough time to watch {serial_name} and left with {ceil(diff)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {ceil(diff)} more minutes.")