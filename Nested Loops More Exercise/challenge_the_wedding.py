customers_man = int(input())
customers_woman = int(input())
total_tables = int(input())

tables = 0

for man in range(1, customers_man + 1):
    for woman in range(1, customers_woman + 1):
        tables += 1
        if tables > total_tables:
            break
        print(f"({man} <-> {woman})", end=' ')
