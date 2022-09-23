best = 0
best_player = 0
input_line = input()
while input_line != "END":
    player_name = input_line
    goals = int(input())
    if goals > best:
        best = goals
        best_player = player_name
    if goals >= 10:
        break

    input_line = input()
print(f"{best_player} is the best player!")
if best >= 3:
    print(f"He has scored {best} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best} goals.")