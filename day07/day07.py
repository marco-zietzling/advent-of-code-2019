import itertools
import intcode.intcode_computer as comp
import os

print("advent of code 2019 - day 7")

# day 7 - part 1
input_file = os.path.join(os.getcwd(), "input.txt")
phase_settings = [0, 1, 2, 3, 4]
max_thruster = -999

for permutation in itertools.permutations(phase_settings, 5):
    amp_a = comp.IntcodeComputer("A", input_file)
    amp_a.provide_arguments([permutation[0]] + [0])
    amp_a.execute()
    result_a = amp_a.consume_output()

    amp_b = comp.IntcodeComputer("B", input_file)
    amp_b.provide_arguments([permutation[1]] + result_a)
    amp_b.execute()
    result_b = amp_b.consume_output()

    amp_c = comp.IntcodeComputer("C", input_file)
    amp_c.provide_arguments([permutation[2]] + result_b)
    amp_c.execute()
    result_c = amp_c.consume_output()

    amp_d = comp.IntcodeComputer("D", input_file)
    amp_d.provide_arguments([permutation[3]] + result_c)
    amp_d.execute()
    result_d = amp_d.consume_output()

    amp_e = comp.IntcodeComputer("E", input_file)
    amp_e.provide_arguments([permutation[4]] + result_d)
    amp_e.execute()
    result_e = amp_e.consume_output()

    if result_e[0] > max_thruster:
        max_thruster = result_e[0]

# result = 118936
print(f"max thruster result = {max_thruster}")

# day 7 - part 2
phase_settings = [5, 6, 7, 8, 9]
max_thruster = -999

for permutation in itertools.permutations(phase_settings, 5):

    # first iteration
    amp_a = comp.IntcodeComputer("A", input_file)
    amp_a.provide_arguments([permutation[0]] + [0])
    amp_a.execute()
    result_a = amp_a.consume_output()

    amp_b = comp.IntcodeComputer("B", input_file)
    amp_b.provide_arguments([permutation[1]] + result_a)
    amp_b.execute()
    result_b = amp_b.consume_output()

    amp_c = comp.IntcodeComputer("C", input_file)
    amp_c.provide_arguments([permutation[2]] + result_b)
    amp_c.execute()
    result_c = amp_c.consume_output()

    amp_d = comp.IntcodeComputer("D", input_file)
    amp_d.provide_arguments([permutation[3]] + result_c)
    amp_d.execute()
    result_d = amp_d.consume_output()

    amp_e = comp.IntcodeComputer("E", input_file)
    amp_e.provide_arguments([permutation[4]] + result_d)
    amp_e_exit_code = amp_e.execute()
    result_e = amp_e.consume_output()

    while amp_e_exit_code != 99:
        amp_a.provide_arguments(result_e)
        amp_a.execute()
        result_a = amp_a.consume_output()

        amp_b.provide_arguments(result_a)
        amp_b.execute()
        result_b = amp_b.consume_output()

        amp_c.provide_arguments(result_b)
        amp_c.execute()
        result_c = amp_c.consume_output()

        amp_d.provide_arguments(result_c)
        amp_d.execute()
        result_d = amp_d.consume_output()

        amp_e.provide_arguments(result_d)
        amp_e_exit_code = amp_e.execute()
        result_e = amp_e.consume_output()

    if result_e[0] > max_thruster:
        max_thruster = result_e[0]

# result = 57660948
print(f"max thruster result = {max_thruster}")
