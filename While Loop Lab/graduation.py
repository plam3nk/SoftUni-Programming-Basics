name = input()

grades_sum = 0
years = 0
failed_years = 0
average_grade = 0

while True:
    grade = float(input())
    if grade >= 4.00:
        grades_sum += grade
    years += 1

    if grade < 4:
        failed_years += 1
        if failed_years == 2:
            print(f"{name} has been excluded at {years} grade")
            break
        years -= 1

    if years == 12:
        average_grade = grades_sum / 12
        print(f"{name} graduated. Average grade: {average_grade:.2f}")
        break
