holidays = int(input())

norm_min = 30000
workdays = 365 - holidays

playtime_work_days = workdays * 63
playtime_off_days = holidays * 127
all_time = playtime_work_days + playtime_off_days
diff = abs(30000 - all_time)
diff_hours = diff // 60
diff_minutes =  diff % 60

if norm_min < all_time:
    print(f"Tom will run away")
    print(f"{diff_hours} hours and {diff_minutes} minutes more for play")
else:
    print(f"Tom sleeps well")
    print(f"{diff_hours} hours and {diff_minutes} minutes less for play")