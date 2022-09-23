actor_name = input()
points_of_academy = float(input())
amount_judges = int(input())

points = points_of_academy

for n in range(1, amount_judges + 1):
    judge_name = input()
    points_from_judge = float(input())

    points = points + len(judge_name) * points_from_judge / 2
    if points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
        break

diff = 1250.5 - points

if points <= 1250.5:
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")

