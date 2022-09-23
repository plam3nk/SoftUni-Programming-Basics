# •	Пакет химикали - 5.80 лв.
# •	Пакет маркери - 7.20 лв.
# •	Препарат - 1.20 лв (за литър)
pens_amount = int(input())
marker_amount = int(input())
preparat_lt = int(input())
discount = int(input())

price_pens = pens_amount * 5.8
price_markers = marker_amount * 7.2
price_preparat = preparat_lt * 1.2

sum_without_discount = price_pens + price_markers + price_preparat
sum = sum_without_discount - (sum_without_discount * discount / 100)
print(sum)
