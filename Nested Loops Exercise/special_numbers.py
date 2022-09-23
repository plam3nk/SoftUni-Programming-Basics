number = int(input())
for current_number in range(1111, 10000):
    is_special = True
    current_number_string = str(current_number)
    for digit in current_number_string:
        digit_int = int(digit)
        if digit_int == 0 or number % digit_int != 0:
            is_special = False
            break
    if is_special:
        print(current_number_string, end=' ')

