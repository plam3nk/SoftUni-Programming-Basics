text = input()

letter_a = 1
letter_e = 2
letter_i = 3
letter_o = 4
letter_u = 5

total = 0

for letter in text:
    if letter == "a":
        total += letter_a
    if letter == "e":
        total += letter_e
    if letter == "i":
        total += letter_i
    if letter == "o":
        total += letter_o
    if letter == "u":
        total += letter_u
print(total)
