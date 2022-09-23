destination = input()

money_sum = 0
while destination != "End":
    money_for_vacation = float(input())
    money_sum = 0
    while money_sum < money_for_vacation:
        current_money = float(input())
        money_sum += current_money

    print(f"Going to {destination}!")
    destination = input()
