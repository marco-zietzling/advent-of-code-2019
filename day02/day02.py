import intcode.intcode_computer as comp

import os

print("advent of code 2019 - day 2")


def patch_input(instructions: list, noun: int, verb: int):
    instructions[1] = noun
    instructions[2] = verb


# day 2 - part 1
input_file = os.path.join(os.getcwd(), "input.txt")
computer = comp.IntcodeComputer("part 1", input_file)

patch_input(computer.instructions, 12, 2)
computer.execute()
part1 = computer.instructions[0]

# result = 4945026
print("part 1: " + str(part1))

# day 2 - part 2
solution_noun = 0
solution_verb = 0

for noun in range(0, 100):
    for verb in range(0, 100):
        computer = comp.IntcodeComputer("part 2", input_file)
        patch_input(computer.instructions, noun, verb)
        computer.execute()
        result = computer.instructions[0]

        if result == 19690720:
            print(f"input found: noun={noun} and verb={verb}")
            solution_noun = noun
            solution_verb = verb

result = 100 * solution_noun + solution_verb

# result = 5296
print(f"part 2: noun={solution_noun} and verb={solution_verb} and result = {result}")
