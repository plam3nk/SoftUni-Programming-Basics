movie_name = input()
total_tickets = 0
total_tickets_kid = 0
total_tickets_standard = 0
total_tickets_student = 0
while movie_name != "Finish":
    free_seats = int(input())
    student_ticket_count = 0
    kid_ticket_count = 0
    standard_ticket_count = 0
    for seat in range(1, free_seats + 1):
        type_ticket = input()
        if type_ticket == "End":
            break
        if type_ticket == "student":
            student_ticket_count += 1
        elif type_ticket == "standard":
            standard_ticket_count += 1
        elif type_ticket == "kid":
            kid_ticket_count += 1
    total_tickets_per_movie = student_ticket_count + kid_ticket_count + standard_ticket_count
    percent_tickets_per_movie = total_tickets_per_movie / free_seats * 100
    print(f"{movie_name} - {percent_tickets_per_movie:.2f}% full.")
    total_tickets += total_tickets_per_movie
    total_tickets_kid += kid_ticket_count
    total_tickets_student += student_ticket_count
    total_tickets_standard += standard_ticket_count

    movie_name = input()

percent_kid = total_tickets_kid / total_tickets * 100
percent_student = total_tickets_student / total_tickets * 100
percent_standard = total_tickets_standard / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{percent_student:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kid:.2f}% kids tickets.")

