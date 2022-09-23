start = int(input())
final = int(input())
magic_number = int(input())
combination = 0
is_not_found = True
is_found = False
for number_one in range(start, final + 1):
    for number_two in range(start, final + 1):
        combination += 1
        if number_one + number_two == magic_number:
            is_not_found = False
            is_found = True
            print(f"Combination N:{combination} ({number_one} + {number_two} = {magic_number})")
            break
    if is_found:
        break
if is_not_found:
    print(f"{combination} combinations - neither equals {magic_number}")
