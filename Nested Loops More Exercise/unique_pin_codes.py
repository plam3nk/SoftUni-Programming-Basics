upper_limit_first_number = int(input())
upper_limit_second_number = int(input())
upper_limit_third_number = int(input())

for first_number in range(1, upper_limit_first_number + 1):
    if first_number % 2 != 0:
        continue
    for second_number in range(2, upper_limit_second_number + 1):
        for third_number in range(1, upper_limit_third_number + 1):
            is_not_prime = False
            if third_number % 2 != 0:
                continue
            for num in range(2, second_number):
                if second_number % num == 0:
                    is_not_prime = True
            if is_not_prime:
                continue
            print(f"{first_number} {second_number} {third_number}")
