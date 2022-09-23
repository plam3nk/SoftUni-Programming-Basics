from math import ceil

days_training = int(input())
kilometres_first_day = float(input())
kilometres = kilometres_first_day
total_kilometres = kilometres_first_day
for day in range(1, days_training + 1):
    percent_increase = int(input())
    kilometres_increase = kilometres * percent_increase / 100
    kilometres += kilometres_increase
    total_kilometres += kilometres
diff = abs(total_kilometres - 1000)
if total_kilometres >= 1000:
    print(f"You've done a great job running {ceil(diff)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(diff)} more kilometers")