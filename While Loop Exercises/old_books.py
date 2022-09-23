looking_book = input()

checked_books = 0
is_not_there = False
user_input = input()

while user_input != looking_book:
    if user_input == "No More Books":
        is_not_there = True
        break
    checked_books += 1
    user_input = input()

if is_not_there:
    print("The book you search is not here!")
    print(f"You checked {checked_books} books.")
else:
    print(f"You checked {checked_books} books and found it.")



