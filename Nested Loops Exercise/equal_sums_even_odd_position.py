first_number = int(input())
second_number = int(input())

for current_number in range(first_number, second_number + 1):
    current_number_string = str(current_number)
    odd_number_sum = 0
    even_number_sum = 0
    for index, digit in enumerate(current_number_string):
        if index % 2 == 0:
            odd_number_sum += int(digit)
        else:
            even_number_sum += int(digit)
    if odd_number_sum == even_number_sum:
        print(current_number_string, end=" ")

