team = input()
type_souvenir = input()
amount_souvenirs = int(input())
price = 0
stock_is_not_valid = False
team_is_not_valid = False
if team == "Argentina":
    if type_souvenir == "flags":
        price = 3.25
    elif type_souvenir == "caps":
        price = 7.20
    elif type_souvenir == "posters":
        price = 5.10
    elif type_souvenir == "stickers":
        price = 1.25
    else:
        stock_is_not_valid = True
elif team == "Brazil":
    if type_souvenir == "flags":
        price = 4.20
    elif type_souvenir == "caps":
        price = 8.50
    elif type_souvenir == "posters":
        price = 5.35
    elif type_souvenir == "stickers":
        price = 1.20
    else:
        stock_is_not_valid = True
elif team == "Croatia":
    if type_souvenir == "flags":
        price = 2.75
    elif type_souvenir == "caps":
        price = 6.90
    elif type_souvenir == "posters":
        price = 4.95
    elif type_souvenir == "stickers":
        price = 1.10
    else:
        stock_is_not_valid = True
elif team == "Denmark":
    if type_souvenir == "flags":
        price = 3.10
    elif type_souvenir == "caps":
        price = 6.50
    elif type_souvenir == "posters":
        price = 4.80
    elif type_souvenir == "stickers":
        price = 0.90
    else:
        stock_is_not_valid = True
else:
    team_is_not_valid = True
total_price = price * amount_souvenirs
if team_is_not_valid:
    print(f"Invalid country!")
elif stock_is_not_valid:
    print("Invalid stock!")
else:
    print(f"Pepi bought {amount_souvenirs} {type_souvenir} of {team} for {total_price:.2f} lv.")