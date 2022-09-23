students = int(input())

bad_grade_counter = 0
decent_grade_counter = 0
good_grade_counter = 0
very_good_grade_counter = 0
grades_sum = 0
for student in range(1, students + 1):
    grade = float(input())
    if grade < 3:
        bad_grade_counter += 1
        grades_sum += grade
    elif grade < 4:
        decent_grade_counter += 1
        grades_sum += grade
    elif grade < 5:
        good_grade_counter += 1
        grades_sum += grade
    else:
        very_good_grade_counter += 1
        grades_sum += grade

average_grade = grades_sum / students
bad_grade_percent = bad_grade_counter / students * 100
decent_grade_percent = decent_grade_counter / students * 100
good_grade_percent = good_grade_counter / students * 100
very_good_grade_percent = very_good_grade_counter / students * 100

print(f"Top students: {very_good_grade_percent:.2f}%")
print(f"Between 4.00 and 4.99: {good_grade_percent:.2f}%")
print(f"Between 3.00 and 3.99: {decent_grade_percent:.2f}%")
print(f"Fail: {bad_grade_percent:.2f}%")
print(f"Average: {average_grade:.2f}")


