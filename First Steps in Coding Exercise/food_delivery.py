# •	Пилешко меню –  10.35 лв.
# •	Меню с риба – 12.40 лв.
# •	Вегетарианско меню  – 8.15 лв.

chicken_menus = int(input())
fish_menus = int(input())
veg_menus = int(input())

price_chicken = chicken_menus * 10.35
price_fish = fish_menus * 12.4
price_veg = veg_menus * 8.15

sum_of_menus = price_chicken + price_fish + price_veg
dessert = sum_of_menus * 20/100
total = sum_of_menus + dessert + 2.5
print(total)