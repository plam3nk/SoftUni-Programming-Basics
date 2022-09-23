from math import floor

amount_tournaments = int(input())
start_points = int(input())

winner_in_tournaments = 0
points_W = 0
points_F = 0
points_SF = 0
points = start_points

for n in range(1, amount_tournaments + 1):
    stage_in_tournament = input()
    if stage_in_tournament == "W":
        winner_in_tournaments += 1
        points = points + 2000
    elif stage_in_tournament == "F":
        points = points + 1200
    elif stage_in_tournament == "SF":
        points = points + 720

points_tournament = points - start_points

percent_winner_in_tournaments = winner_in_tournaments / amount_tournaments * 100
average_win_points = points_tournament / amount_tournaments

print(f"Final points: {points}")
print(f"Average points: {floor(average_win_points)}")
print(f"{percent_winner_in_tournaments:.2f}%")
