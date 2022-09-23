capacity_of_stadium = int(input())
fans_total = int(input())

fans_sector_A = 0
fans_sector_B = 0
fans_sector_V = 0
fans_sector_G = 0

for fan in range(1, fans_total + 1):
    sector = input()
    if sector == "A":
        fans_sector_A += 1
    elif sector == "B":
        fans_sector_B += 1
    elif sector == "V":
        fans_sector_V += 1
    elif sector == "G":
        fans_sector_G += 1

fans_sector_A_percent = fans_sector_A / fans_total * 100
fans_sector_B_percent = fans_sector_B / fans_total * 100
fans_sector_V_percent = fans_sector_V / fans_total * 100
fans_sector_G_percent = fans_sector_G / fans_total * 100
fans_stadium_percent = fans_total / capacity_of_stadium * 100

print(f"{fans_sector_A_percent:.2f}%")
print(f"{fans_sector_B_percent:.2f}%")
print(f"{fans_sector_V_percent:.2f}%")
print(f"{fans_sector_G_percent:.2f}%")
print(f"{fans_stadium_percent:.2f}%")


