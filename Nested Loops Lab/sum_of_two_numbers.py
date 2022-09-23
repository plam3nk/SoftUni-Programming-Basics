start = int(input())
end = int(input())
magic_number = int(input())

combination = 0
is_found = False

for number in range(start, end + 1):
    for number2 in range(start, end + 1):

        combination += 1
        if number + number2 == magic_number:
            is_found = True
            break
    if is_found:
        break
if is_found:
    print(f"Combination N:{combination} ({number} + {number2} = {magic_number})")
else:
    print(f"{combination} combinations - neither equals {magic_number}")
