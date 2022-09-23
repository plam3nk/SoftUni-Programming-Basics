coins = float(input()) * 100
coins = int(coins)
current_coins = 0

while coins != 0:
    if coins >= 200:
        current_coins += 1
        coins -= 200
    elif coins >= 100:
        current_coins += 1
        coins -= 100
    elif coins >= 50:
        current_coins += 1
        coins -= 50
    elif coins >= 20:
        current_coins += 1
        coins -= 20
    elif coins >= 10:
        current_coins += 1
        coins -= 10
    elif coins >= 5:
        current_coins += 1
        coins -= 5
    elif coins >= 2:
        current_coins += 1
        coins -= 2
    elif coins >= 1:
        current_coins += 1
        coins -= 1
print(current_coins)


