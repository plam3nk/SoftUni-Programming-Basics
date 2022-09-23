number_N = int(input())
number_M = int(input())
number_S = int(input())
number = number_M
while number != number_N:
    if number % 2 == 0 and number % 3 == 0:
        if number == number_S:
            break
        print(number, end=" ")
    number -= 1