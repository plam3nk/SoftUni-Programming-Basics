number = int(input())

left_sum = 0
right_sum = 0

for num in range(1, number + 1):
    num = int(input())
    left_sum = left_sum + num
for num in range(1, number + 1):
    num = int(input())
    right_sum = right_sum + num
diff = abs(left_sum - right_sum)
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {diff}")