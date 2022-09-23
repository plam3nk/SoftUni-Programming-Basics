lucky_number = int(input())

for number in range(1111, 10000):
    number_string = str(number)
    digit0 = 0
    digit1 = 0
    digit2 = 0
    digit3 = 0
    for index, digit in enumerate(number_string):
        if index == 0:
            digit0 = int(digit)
        elif index == 1:
            digit1 = int(digit)
        elif index == 2:
            digit2 = int(digit)
        elif index == 3:
            digit3 = int(digit)
    if digit1 == 0 or digit2 == 0 or digit3 == 0 or digit0 == 0:
        continue

    first_digits = digit0 + digit1
    second_digits = digit2 + digit3
    if first_digits == second_digits and lucky_number % first_digits == 0:
        print(number, end=' ')