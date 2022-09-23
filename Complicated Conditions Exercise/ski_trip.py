days_staying = int(input())
type_room = input()
feedback = input()

price = 0
sleeps = days_staying - 1
room_for_one_person = 18 * sleeps
apartment = 25 * sleeps
president_apartment = 35 * sleeps

if 10 > days_staying:
    if type_room == "apartment":
        price = apartment * 0.70
    elif type_room == "president apartment":
        price = president_apartment * 0.90
    elif type_room == "room_for_one_person":
        price = room_for_one_person
elif 10 <= days_staying <= 15:
    if type_room == "apartment":
        price = apartment * 0.65
    elif type_room == "president apartment":
        price = president_apartment * 0.85
    elif type_room == "room for one person":
        price = room_for_one_person
elif days_staying > 15:
    if type_room == "apartment":
        price = apartment * 0.50
    elif type_room == "president apartment":
        price = president_apartment * 0.80
    elif type_room == "room for one person":
        price = room_for_one_person

if feedback == "positive":
    price = price * 1.25
elif feedback == "negative":
    price = price * 0.90
print(f"{price:.2f}")