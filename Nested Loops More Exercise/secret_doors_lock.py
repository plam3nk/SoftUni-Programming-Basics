ones_limit = int(input())
tens_limit = int(input())
hundreds_limit = int(input())

for number_one in range(1, ones_limit + 1):
    if number_one % 2 != 0:
        continue
    for number_two in range(2, tens_limit + 1):
        is_not_prime = False
        for num in range(2, number_two):
            if number_two % num == 0:
                is_not_prime = True
                break
        if is_not_prime:
            continue
        for number_three in range(1, hundreds_limit + 1):
            if number_three % 2 != 0:
                continue
            print(f"{number_one} {number_two} {number_three}")
