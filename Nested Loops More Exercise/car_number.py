start = int(input())
final = int(input())

for number_one in range(start, final + 1):
    for number_two in range(start, final + 1):
        for number_three in range(start, final + 1):
            for number_four in range(start, final + 1):
                is_valid = False
                is_even = False
                is_greater = False
                sum_number_two_three = number_two + number_three
                if number_one % 2 == 0 and number_four % 2 != 0:
                    is_valid = True
                if number_one % 2 != 0 and number_four % 2 == 0:
                    is_valid = True
                if number_one > number_four:
                    is_greater = True
                if sum_number_two_three % 2 == 0:
                    is_even = True
                if is_valid and is_even and is_greater:
                    print(f"{number_one}{number_two}{number_three}{number_four}", end=' ')