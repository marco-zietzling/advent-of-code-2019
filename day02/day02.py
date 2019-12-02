print("advent of code 2019 - day 2")


def prepare_input():
    with open("input.txt") as file:
        for line in file:
            return [int(i) for i in line.split(",")]


def patch_input(input, noun, verb):
    input[1] = noun
    input[2] = verb


def run_program(input):
    current_index = 0

    while True:
        opcode = input[current_index]
        index1 = input[current_index + 1]
        index2 = input[current_index + 2]
        index_target = input[current_index + 3]

        # terminate
        if opcode == 99:
            # print("program terminated - value at position '0'=" + str(input[0]))
            return input[0]

        # addition
        elif opcode == 1:
            input[index_target] = input[index1] + input[index2]

        # multiplication
        elif opcode == 2:
            input[index_target] = input[index1] * input[index2]

        else:
            print(f"program exception - unknown opcode {opcode}")
            break

        current_index = current_index + 4


# day 2 - part 1
input = prepare_input()
patch_input(input, 12, 2)
part1 = run_program(input)

# result = 4945026
print("part 1: " + str(part1))

# day 2 - part 2
solution_noun = 0
solution_verb = 0

for noun in range(0, 100):
    for verb in range(0, 100):
        input = prepare_input()
        patch_input(input, noun, verb)
        result = run_program(input)
        if result == 19690720:
            print(f"input found: noun={noun} and verb={verb}")
            solution_noun = noun
            solution_verb = verb

result = 100 * solution_noun + solution_verb

# result = 5296
print(f"part 2: noun={solution_noun} and verb={solution_verb} and result = {result}")
