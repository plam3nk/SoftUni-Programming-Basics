letter_start = input()
letter_end = input()
letter_skip = input()

combinations = 0

for letter_one in range(ord(letter_start), ord(letter_end) + 1):
    for letter_two in range(ord(letter_start), ord(letter_end) + 1):
        for letter_three in range(ord(letter_start), ord(letter_end) + 1):
            if letter_one == ord(letter_skip) or letter_two == ord(letter_skip) or letter_three == ord(letter_skip):
                continue
            print(f"{chr(letter_one)}{chr(letter_two)}{chr(letter_three)}", end=' ')
            combinations += 1
print(combinations)
