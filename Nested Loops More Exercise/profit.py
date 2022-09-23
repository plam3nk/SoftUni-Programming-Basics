coins_ones = int(input())
coins_twos = int(input())
paper_fives = int(input())
total_sum = int(input())

for ones in range(0, coins_ones + 1):
    for twos in range(0, coins_twos + 1):
        for fives in range(0, paper_fives + 1):
            sum_twos = twos * 2
            sum_fives = fives * 5
            if ones + sum_twos + sum_fives == total_sum:
                print(f"{ones} * 1 lv. + {twos} * 2 lv. + {fives} * 5 lv. = {total_sum} lv.")