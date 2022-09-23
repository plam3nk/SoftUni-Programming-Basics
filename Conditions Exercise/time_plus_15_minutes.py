hours = int(input())
minutes = int(input())

minutes_15 = minutes + 15

if minutes_15 > 59:
    minutes_15 = minutes_15 - 60
    hours = hours + 1
if hours > 23:
    hours = 0

if minutes_15 < 10:
    print(f"{hours}:0{minutes_15}")
else:
    print(f"{hours}:{minutes_15}")