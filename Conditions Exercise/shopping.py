budget = float(input())
videocards = int(input())
processors = int(input())
ram = int(input())

p_videocards = videocards * 250
p_processors = p_videocards * 0.35 * processors
p_ram = p_videocards * 0.10 * ram

final_sum = p_videocards + p_processors + p_ram

if videocards > processors:
    final_sum = final_sum * 0.85

difference = abs(budget - final_sum)

if budget >= final_sum:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")