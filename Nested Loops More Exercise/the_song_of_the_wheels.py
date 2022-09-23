control_number = int(input())

counter = 0
for a in range(1, 10):
    for b in range(1, 10):
        if a >= b:
            continue
        for c in range(1, 10):
            for d in range(1, 10):
                if c <= d:
                    continue
                if a * b + c * d == control_number:
                    counter += 1
                    print(f"{a}{b}{c}{d}", end=" ")
                    if counter == 4:
                        magic_a = a
                        magic_b = b
                        magic_c = c
                        magic_d = d
print()
if counter < 4:
    print("No!")
else:
    print(f"Password: {magic_a}{magic_b}{magic_c}{magic_d}")