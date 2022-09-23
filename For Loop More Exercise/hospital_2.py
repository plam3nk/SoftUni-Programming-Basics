period = int(input())

total_examined = 0
total_unexamined = 0
doctors = 7
for day in range(1, period + 1):
    number_of_patients = int(input())
    examined_patients_per_day = 0
    unexamined_patients_per_day = 0

    if number_of_patients > doctors:
        examined_patients_per_day = doctors
        unexamined_patients_per_day = number_of_patients - examined_patients_per_day
    if number_of_patients <= doctors:
        examined_patients_per_day += number_of_patients

    total_examined += examined_patients_per_day
    total_unexamined += unexamined_patients_per_day

    if day % 3 == 0:
        if total_unexamined < total_examined:
            doctors += 1

print(f"Treated patients: {total_examined}.")
print(f"Untreated patients: {total_unexamined}.")

