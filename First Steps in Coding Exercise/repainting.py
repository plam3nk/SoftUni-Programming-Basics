# •	Предпазен найлон - 1.50 лв. за кв. метър
# •	Боя - 14.50 лв. за литър
# •	Разредител за боя - 5.00 лв. за литър

nylon = int(input())
paint = int(input())
thinner = int(input())
work_time = int(input())

price_nylon = (nylon + 2) * 1.5
price_paint = (paint * 1.1) * 14.5
price_thinner = thinner * 5
price_of_bags = 0.4

all_price = price_nylon + price_paint + price_thinner + price_of_bags
price_of_hourwork = all_price * 30 / 100
price_of_work = price_of_hourwork * work_time
total = all_price + price_of_work
print(total)
