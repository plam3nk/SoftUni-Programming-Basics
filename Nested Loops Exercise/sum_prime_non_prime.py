input_line = input()
prime_number_sum = 0
non_prime_number_sum = 0
while input_line != "stop":
    current_number = int(input_line)
    if current_number < 0:
        print("Number is negative.")
    else:
        number_is_prime = True
        for number in range(2, current_number):
            if current_number % number == 0:
                number_is_prime = False
                break
        if number_is_prime:
            prime_number_sum += current_number
        else:
            non_prime_number_sum += current_number

    input_line = input()

print(f"Sum of all prime numbers is: {prime_number_sum}")
print(f"Sum of all non prime numbers is: {non_prime_number_sum}")
