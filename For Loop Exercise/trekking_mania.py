group_climbers = int(input())

musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
for n in range(1, group_climbers + 1):
    people_in_group = int(input())
    if people_in_group < 6:
        musala += people_in_group
    elif people_in_group < 13:
        monblan += people_in_group
    elif people_in_group < 26:
        kilimandjaro += people_in_group
    elif people_in_group < 41:
        k2 += people_in_group
    elif people_in_group >= 41:
        everest += people_in_group

total = musala + monblan + kilimandjaro + k2 + everest

percent_musala = musala / total * 100
percent_monblan = monblan / total * 100
percent_kilimandjaro = kilimandjaro / total * 100
percent_k2 = k2 / total * 100
percent_everest = everest / total * 100

print(f"{percent_musala:.2f}%")
print(f"{percent_monblan:.2f}%")
print(f"{percent_kilimandjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")