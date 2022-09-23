from math import floor, ceil

vineyard = int(input())
grapes_per_meter2 = float(input())
litres_need = int(input())
workers = int(input())

harvest = vineyard * grapes_per_meter2
grapes_for_wine = harvest * 0.40
wine = grapes_for_wine / 2.5
diff = abs(wine - litres_need)
diff_per_worker = 0
if wine >= litres_need:
    diff_per_worker = diff / workers
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(diff)} liters left -> {ceil(diff_per_worker)} liters per person.")
else:
    print(f"It will be a tough winter! More {floor(diff)} liters wine needed.")