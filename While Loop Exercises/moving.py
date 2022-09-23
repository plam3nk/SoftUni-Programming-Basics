width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())

free_space = width_free_space * length_free_space * height_free_space

user_input = input()

while user_input != "Done":
    boxes = int(user_input)
    free_space -= boxes
    if free_space < 0:
        print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
        break
    user_input = input()
if free_space >= 0:
    print(f"{free_space} Cubic meters left.")
