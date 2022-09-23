number_of_jury = int(input())

total_grades_sum = 0
grades_counter = 0

presentation_name = input()

while presentation_name != "Finish":
    grade_sum_per_presentation = 0
    for grades in range(number_of_jury):
        current_grade = float(input())
        grade_sum_per_presentation += current_grade
        grades_counter += 1
    average_grade = grade_sum_per_presentation / number_of_jury
    print(f"{presentation_name} - {average_grade:.2f}.")
    total_grades_sum += grade_sum_per_presentation
    presentation_name = input()

total_average = total_grades_sum / grades_counter
print(f"Student's final assessment is {total_average:.2f}.")
