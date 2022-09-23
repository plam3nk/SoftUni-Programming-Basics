last_sector = input()
rows_first_sector = int(input())
seats_odd_row = int(input())

seat_counter = 0
seats_even_row = seats_odd_row + 2
for sector in range(ord("A"), ord(last_sector) + 1):
    for row in range(1, rows_first_sector + 1):
        if row % 2 != 0:
            for seats in range(1, seats_odd_row + 1):
                seats_character = 96 + seats
                print(f"{chr(sector)}{row}{chr(seats_character)}")
                seat_counter += 1
        elif row % 2 == 0:
            for seats in range(1, seats_even_row + 1):
                seats_character = 96 + seats
                print(f"{chr(sector)}{row}{chr(seats_character)}")
                seat_counter += 1
    rows_first_sector += 1
print(seat_counter)
