poor_grades = int(input())

user_input = input()
poor_grades_count = 0
sum_grades = 0
last_problem = 0
grade_count = 0

while user_input != "Enough":
    grade_input = int(input())
    grade_count += 1
    sum_grades += grade_input
    if grade_input <= 4:
        poor_grades_count += 1
    if poor_grades_count == poor_grades:
        print(f"You need a break, {poor_grades} poor grades.")
        break
    last_problem = user_input
    user_input = input()

avg_grade = sum_grades / grade_count

if user_input == "Enough":
    print(f"Average score: {avg_grade:.2f}")
    print(f"Number of problems: {grade_count}")
    print(f"Last problem: {last_problem}")


