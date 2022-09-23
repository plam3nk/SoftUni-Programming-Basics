volume_of_pool = int(input())
debit_first_pipe = int(input())
debit_second_pipe = int(input())
hours_worker_missing = float(input())

litres_from_first_pipe = debit_first_pipe * hours_worker_missing
litres_from_second_pipe = debit_second_pipe * hours_worker_missing
litres_both = litres_from_first_pipe + litres_from_second_pipe

pool_volume = litres_both / volume_of_pool * 100
diff = litres_both - volume_of_pool

first_pipe_percent = litres_from_first_pipe / litres_both * 100
second_pipe_percent = litres_from_second_pipe / litres_both * 100
if litres_both <= volume_of_pool:
    print(f"The pool is {pool_volume:.2f}% full. Pipe 1: {first_pipe_percent:.2f}%. "
          f"Pipe 2: {second_pipe_percent:.2f}%.")
else:
    print(f"For {hours_worker_missing:.2f} hours the pool overflows with {diff:.2f} liters.")
