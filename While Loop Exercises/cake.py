cake_length = int(input())
cake_width = int(input())

cake_pieces = cake_width * cake_length
input_line = input()
while input_line != "STOP":
    piece_taken = int(input_line)
    cake_pieces -= piece_taken
    if cake_pieces < 0:
        print(f"No more cake left! You need {abs(cake_pieces)} pieces more.")
        break
    input_line = input()
if cake_pieces >= 0:
    print(f"{cake_pieces} pieces are left.")
