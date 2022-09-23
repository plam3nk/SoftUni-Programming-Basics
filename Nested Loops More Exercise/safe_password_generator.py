a = int(input())
b = int(input())
max_passwords = int(input())
password_counter = 0
A = 35
B = 64
for x in range(1, a + 1):
    for y in range(1, b + 1):
        if A == 56:
            A = 35
        if B == 97:
            B = 64
        print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")
        A += 1
        B += 1
        password_counter += 1
        if password_counter == max_passwords:
            break
    if password_counter == max_passwords:
        break


