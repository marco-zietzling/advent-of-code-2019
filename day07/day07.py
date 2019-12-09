import itertools
import intcode.intcode_computer as comp
import os

print("advent of code 2019 - day 7")

# day 7 - part 1
phase_settings = [0, 1, 2, 3, 4]
max_thruster = -999

for permutation in itertools.permutations(phase_settings, 5):
    amp_a = comp.IntcodeComputer("A", "input.txt")
    result_a = amp_a.run_program([permutation[0], 0])[0]

    amp_b = comp.IntcodeComputer("B", "input.txt")
    result_b = amp_b.run_program([permutation[1], result_a])[0]

    amp_c = comp.IntcodeComputer("C", "input.txt")
    result_c = amp_c.run_program([permutation[2], result_b])[0]

    amp_d = comp.IntcodeComputer("D", "input.txt")
    result_d = amp_d.run_program([permutation[3], result_c])[0]

    amp_e = comp.IntcodeComputer("E", "input.txt")
    result_e = amp_e.run_program([permutation[4], result_d])[0]

    if result_e > max_thruster:
        max_thruster = result_e

# result = 118936
print(f"max thruster result = {max_thruster}")

# day 7 - part 2
# phase_settings = [5, 6, 7, 8, 9]
#
# for permutation in itertools.permutations(phase_settings, 5):
#     amp_a = comp.IntcodeComputer("A", "input.txt")
#     result_a = amp_a.run_program([permutation[0], 0])
#     print(result_a)
