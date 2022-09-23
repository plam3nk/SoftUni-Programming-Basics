import sys

number = int(input())

total = 0
max_number = -sys.maxsize

for n in range(1, number + 1):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    total = total + current_number
total = total - max_number
if max_number == total:
    print("Yes")
    print(f"Sum = {max_number}")
diff = abs(max_number - total)
if max_number != total:
    print("No")
    print(f"Diff = {diff}")