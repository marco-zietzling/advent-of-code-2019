from collections import defaultdict

print("advent of code 2019 - day 3")

puzzle_range_min = 171309
puzzle_range_max = 643603


# day 4 - part 1

def check_two_adjacent_digits(input_array):
    for i in range(len(input_array) - 1):
        if input_array[i] == input_array[i + 1]:
            return True
    return False


def check_increasing_sequence(input_array):
    for i in range(len(input_array) - 1):
        if input_array[i] > input_array[i + 1]:
            return False
    return True


result_set = set()

for password in range(puzzle_range_min, puzzle_range_max):
    exploded_input = [int(i) for i in str(password)]

    if check_two_adjacent_digits(exploded_input) and check_increasing_sequence(exploded_input):
        result_set.add(password)

# print(result_set)
# result = 1625
print(f"part 1: number of valid passwords = {len(result_set)}")


# day 4 - part 2

def check_larger_groups(input_array):
    input_dict = defaultdict(int)
    for i in input_array:
        input_dict[i] += 1

    return 2 in input_dict.values()


result_set = set()

for password in range(puzzle_range_min, puzzle_range_max):
    exploded_input = [int(i) for i in str(password)]

    if check_two_adjacent_digits(exploded_input) \
            and check_increasing_sequence(exploded_input) \
            and check_larger_groups(exploded_input):
        result_set.add(password)

# print(result_set)
# result = 1111
print(f"part 2: number of valid passwords = {len(result_set)}")
