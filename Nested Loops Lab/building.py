number_of_floors = int(input())
number_of_rooms = int(input())

floor_letter = ''
for floors in range (number_of_floors, 0, -1):
    for rooms in range (number_of_rooms):
        if floors == number_of_floors:
            floor_letter = "L"
        elif floors % 2 == 0:
            floor_letter = "O"
        else:
            floor_letter = "A"
        print(f"{floor_letter}{floors}{rooms}", end=' ')
    print()
