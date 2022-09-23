number = input()
last_digit = number[2]
end_is_5 = False
if last_digit == "5":
    end_is_5 = True
not_found = False
is_found = False
for a in range(1, 10):
    for b in range(9, a, -1):
        for c in range(9):
            for d in range(9, c, -1):
                number_int = int(number)
                sum_all = a + b + c + d
                product = a * b * c * d
                if is_found:
                    break
                if sum_all == product and end_is_5:
                    print(f"{a}{b}{c}{d}")
                    is_found = True
                elif product // sum_all == 3 and number_int % 3 == 0:
                    print(f"{d}{c}{b}{a}")
                    is_found = True

if not is_found:
    print("Nothing found")
    