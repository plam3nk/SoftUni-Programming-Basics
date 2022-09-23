money_for_vacation = float(input())
available_money = float(input())

current_money = available_money
total_days = 0
days_spending = 0

while current_money < money_for_vacation:
    action = input()
    money_action = float(input())

    total_days += 1
    if action == "spend":
        current_money -= money_action
        days_spending += 1
        if current_money < money_action:
            current_money = 0
        if days_spending == 5:
            print("You can't save the money.")
            print(f"{total_days}")
            break
    elif action == "save":
        current_money += money_action
        days_spending = 0
        if current_money >= money_for_vacation:
            print(f"You saved the money for {total_days} days.")
            break
