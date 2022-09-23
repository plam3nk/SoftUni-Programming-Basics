from math import floor

record_in_sec = float(input())
distance_metres = float(input())
time_for_meter_sec = float(input())

time = distance_metres * time_for_meter_sec
delay = floor(distance_metres / 15) * 12.5
all_time = time + delay
diff = all_time - record_in_sec

if all_time < record_in_sec:
    print(f"Yes, he succeeded! The new world record is {all_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")

