increase = 0

total = 0

while increase != "NoMoreMoney":
    increase = input()
    continue
    increase = float(increase)
    if increase >= 0:
        print(f"Increase: {increase:.2f}")
        total += increase
    else:
        print("Invalid operation!")
        print(f"Total: {total:.2f}")
else:
    print(f"Total: {total:.2f}")