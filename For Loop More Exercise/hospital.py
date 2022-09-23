period = int(input())

doctors = 7
examined_patients = 0
unexamined_patients = 0

for days in range(1, period + 1):
    number_of_patients = int(input())
    if days % 3 == 0 and unexamined_patients > examined_patients:
        doctors += 1
    if number_of_patients > doctors:
        examined_patients += doctors
        unexamined_patients += number_of_patients - doctors
    elif number_of_patients <= doctors:
        examined_patients += number_of_patients

print(f"Treated patients: {examined_patients}.")
print(f"Untreated patients: {unexamined_patients}.")
