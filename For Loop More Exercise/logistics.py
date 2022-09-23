cargos = int(input())

price_microbus = 0
price_truck = 0
price_train = 0

microbus_tons = 0
truck_tons = 0
train_tons = 0
for n in range(1, cargos + 1):
    cargo = int(input())
    if cargo < 4:
        microbus_tons += cargo
        price_microbus += 200 * cargo
    elif cargo < 12:
        truck_tons += cargo
        price_truck += 175 * cargo
    elif cargo >= 12:
        train_tons += cargo
        price_train += 120 * cargo

all_tons = microbus_tons + truck_tons + train_tons

microbus_percent = microbus_tons / all_tons * 100
truck_percent = truck_tons / all_tons * 100
train_percent = train_tons / all_tons * 100

average_price = (price_microbus + price_truck + price_train) / all_tons

print(f"{average_price:.2f}")
print(f"{microbus_percent:.2f}%")
print(f"{truck_percent:.2f}%")
print(f"{train_percent:.2f}%")
