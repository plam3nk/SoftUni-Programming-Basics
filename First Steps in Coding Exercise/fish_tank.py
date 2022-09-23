lenght = int(input())
thickness = int(input())
height = int(input())
percent = float(input())

volume = lenght * thickness * height
volume_in_litres = volume / 1000
occupied_space = volume_in_litres * percent / 100
need_litres = volume_in_litres - occupied_space
print(need_litres)