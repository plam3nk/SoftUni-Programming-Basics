moves_amount = int(input())

result = 0
moves_0_9 = 0
moves_10_19 = 0
moves_20_29 = 0
moves_30_39 = 0
moves_40_50 = 0
invalid = 0
for moves in range(1, moves_amount + 1):
    move = int(input())
    if move < 0 or move > 50:
        invalid += 1
        result = result / 2
    elif move < 10:
        moves_0_9 += 1
        result += move * 0.2
    elif move < 20:
        moves_10_19 += 1
        result += move * 0.3
    elif move < 30:
        moves_20_29 += 1
        result += move * 0.4
    elif move < 40:
        moves_30_39 += 1
        result += 50
    elif move <= 50:
        moves_40_50 += 1
        result += 100

moves_0_9_percent = moves_0_9 / moves_amount * 100
moves_10_19_percent = moves_10_19 / moves_amount * 100
moves_20_29_percent = moves_20_29 / moves_amount * 100
moves_30_39_percent = moves_30_39 / moves_amount * 100
moves_40_50_percent = moves_40_50 / moves_amount * 100
invalid_percent = invalid / moves_amount * 100

print(f"{result:.2f}")
print(f"From 0 to 9: {moves_0_9_percent:.2f}%")
print(f"From 10 to 19: {moves_10_19_percent:.2f}%")
print(f"From 20 to 29: {moves_20_29_percent:.2f}%")
print(f"From 30 to 39: {moves_30_39_percent:.2f}%")
print(f"From 40 to 50: {moves_40_50_percent:.2f}%")
print(f"Invalid numbers: {invalid_percent:.2f}%")





