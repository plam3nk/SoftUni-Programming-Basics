number = int(input())

odd_number = 0
even_number = 0

for n in range(number):
    current_number = int(input())
    if n % 2 == 0:
        even_number += current_number
    if n % 2 != 0:
        odd_number += current_number
if odd_number == even_number:
    print("Yes")
    print(f"Sum = {odd_number}")
else:
    diff = abs(odd_number - even_number)
    print("No")
    print(f"Diff = {diff}")
