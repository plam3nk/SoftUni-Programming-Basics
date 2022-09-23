number = int(input())

counter = 1
is_bigger = False
for row in range(1, number + 1):
    for columns in range(1, row + 1):
        print(counter, end = " ")
        counter += 1
        if counter > number:
            is_bigger = True
            break
    print()
    if is_bigger:
        break
