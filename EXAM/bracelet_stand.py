pocket_money_day = float(input())
profit_money_day = float(input())
expense = float(input())
gift_price = float(input())

days = 5

saved_pocket_money = pocket_money_day * 5
profit_money = profit_money_day * 5
total_saved = saved_pocket_money + profit_money
total = total_saved - expense

if total >= gift_price:
    print(f"Profit: {total:.2f} BGN, the gift has been purchased.")
else:
    diff = gift_price - total
    print(f"Insufficient money: {diff:.2f} BGN.")