import random

def write_unique_random_numbers(filename, count):
    numbers = random.sample(range(1, count * 10), count)
    with open(filename, 'w') as f:
        for num in numbers:
            f.write(f"{num}\n")

write_unique_random_numbers('search_input.txt', 50000)