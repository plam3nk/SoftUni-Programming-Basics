
total = 0

while True:
    increase = input()
    if increase == "NoMoreMoney":
        print(f"Total: {total:.2f}")
        break
    else:
        increase = float(increase)
        if increase >= 0:
            print(f"Increase: {increase:.2f}")
            total += increase
        else:
            print("Invalid operation!")
            print(f"Total: {total:.2f}")
            break

