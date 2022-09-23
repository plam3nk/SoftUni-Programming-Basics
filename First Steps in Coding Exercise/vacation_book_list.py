amount_of_pages = int(input())
pages_per_hour = int(input())
amount_of_days = int(input())

all_hours = amount_of_pages // pages_per_hour
hours_per_day = all_hours // amount_of_days

print(hours_per_day)
