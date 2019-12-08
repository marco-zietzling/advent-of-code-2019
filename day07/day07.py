import itertools

print("advent of code 2019 - day 7")


# day 7 - part 1 (copied from day 5, slightly modified)

def read_program():
    with open("input.txt") as file:
        for line in file:
            return [int(i) for i in line.split(",")]


def get_parameter(mode: int, program: list, param: int):
    # position mode
    if mode == 0:
        return int(program[param])
    # immediate mode
    elif mode == 1:
        return int(param)


def run_program(program: list, phase_setting: int, input_signal: int, starting_index: int = 0):
    index = starting_index
    phase_setting_used = False
    input_signal_used = False
    program_output = 9999

    while True:
        instruction = program[index]
        # print(f"instruction = {instruction}")

        instruction_str = str(instruction).zfill(5)
        # print(f"instruction string = {instruction_str}")

        opcode = int(instruction_str[3:])
        param1_mode = int(instruction_str[2])
        param2_mode = int(instruction_str[1])
        # print(f"opcode = {opcode}, p1mode = {param1_mode}, p2mode = {param2_mode}, p3mode = {param3_mode}")

        # halt (and return program output)
        if opcode == 99:
            return (99, index, program_output)

        # addition
        elif opcode == 1:
            arg1 = get_parameter(param1_mode, program, program[index + 1])
            arg2 = get_parameter(param2_mode, program, program[index + 2])
            target_index = program[index + 3]
            program[target_index] = arg1 + arg2
            index = index + 4

        # multiplication
        elif opcode == 2:
            arg1 = get_parameter(param1_mode, program, program[index + 1])
            arg2 = get_parameter(param2_mode, program, program[index + 2])
            target_index = program[index + 3]
            program[target_index] = arg1 * arg2
            index = index + 4

        # read input and save at index
        elif opcode == 3:
            target_index = program[index + 1]
            # input_to_be_used = input("Enter your input: ")
            if not phase_setting_used:
                # print(f"phase setting = {phase_setting}")
                input_to_be_used = phase_setting
                phase_setting_used = True
            elif not input_signal_used:
                # print(f"input signal = {input_signal}")
                input_to_be_used = input_signal
                input_signal_used = True
            else:
                input_to_be_used = -999
                print(f"ERROR: unknown input expected")

            program[target_index] = input_to_be_used
            # print(f"read input {program[target_index]} and stored it at position {target_index}")
            index = index + 2

        # output value at index
        elif opcode == 4:
            target_index = program[index + 1]
            program_output = program[target_index]
            index = index + 2
            # print(f"program output = {program[target_index]}")
            return (4, index, program_output)

        # jump if true
        elif opcode == 5:
            arg1 = get_parameter(param1_mode, program, program[index + 1])
            arg2 = get_parameter(param2_mode, program, program[index + 2])
            if arg1 != 0:
                index = arg2
            else:
                index = index + 3

        # jump if false
        elif opcode == 6:
            arg1 = get_parameter(param1_mode, program, program[index + 1])
            arg2 = get_parameter(param2_mode, program, program[index + 2])

            if arg1 == 0:
                index = arg2
            else:
                index = index + 3

        # less than
        elif opcode == 7:
            arg1 = get_parameter(param1_mode, program, program[index + 1])
            arg2 = get_parameter(param2_mode, program, program[index + 2])
            target_index = program[index + 3]

            if arg1 < arg2:
                program[target_index] = 1
            else:
                program[target_index] = 0

            index = index + 4

        # equals
        elif opcode == 8:
            arg1 = get_parameter(param1_mode, program, program[index + 1])
            arg2 = get_parameter(param2_mode, program, program[index + 2])
            target_index = program[index + 3]

            if arg1 == arg2:
                program[target_index] = 1
            else:
                program[target_index] = 0

            index = index + 4

        else:
            print(f"program exception - unknown opcode = {opcode}")
            break


def run_amplifier(input_program: list, amp_name: str, phase_setting: int, input_signal: int, starting_index: int = 0):
    # print(f"running amplifier {amp_name} with phase setting = {phase_setting} and input signal = {input_signal}")
    output = run_program(input_program, phase_setting, input_signal, starting_index)
    # print(f"result of amplifier {amp_name} = {output}")
    return output


# possible phase settings 0..4
program = read_program()
phase_settings = [0, 1, 2, 3, 4]
max_thruster = -999

for permutation in itertools.permutations(phase_settings, 5):
    (_, _, result_amp_a) = run_amplifier(program.copy(), "A", phase_setting=permutation[0], input_signal=0)
    (_, _, result_amp_b) = run_amplifier(program.copy(), "B", phase_setting=permutation[1], input_signal=result_amp_a)
    (_, _, result_amp_c) = run_amplifier(program.copy(), "C", phase_setting=permutation[2], input_signal=result_amp_b)
    (_, _, result_amp_d) = run_amplifier(program.copy(), "D", phase_setting=permutation[3], input_signal=result_amp_c)
    (_, _, result_amp_e) = run_amplifier(program.copy(), "E", phase_setting=permutation[4], input_signal=result_amp_d)

    if result_amp_e > max_thruster:
        max_thruster = result_amp_e

# result = 118936
print(f"max thruster result = {max_thruster}")

# day 7 - part 2
phase_settings = [5, 6, 7, 8, 9]

# for permutation in itertools.permutations(phase_settings, 5):

result_amp_e = 0  # initial input for amp A is 0
index_a = 0
program_a = program.copy()
index_b = 0
program_b = program.copy()
index_c = 0
program_c = program.copy()
index_d = 0
program_d = program.copy()
index_e = 0
program_e = program.copy()

permutation = [9, 8, 7, 6, 5]
while True:
    (_, index_a, result_amp_a) = run_amplifier(program_a, "A", phase_setting=permutation[0], input_signal=result_amp_e,
                                               starting_index=index_a)
    (_, index_b, result_amp_b) = run_amplifier(program_b, "B", phase_setting=permutation[1], input_signal=result_amp_a,
                                               starting_index=index_b)
    (_, index_c, result_amp_c) = run_amplifier(program_c, "C", phase_setting=permutation[2], input_signal=result_amp_b,
                                               starting_index=index_c)
    (_, index_d, result_amp_d) = run_amplifier(program_d, "D", phase_setting=permutation[3], input_signal=result_amp_c,
                                               starting_index=index_d)
    (return_code_e, index_e, result_amp_e) = run_amplifier(program_e, "E", phase_setting=permutation[4],
                                                           input_signal=result_amp_d, starting_index=index_e)

    print(f"return code amp E = {return_code_e} with result = {result_amp_e}")

    # check for halt
    if return_code_e == 99:
        print(f"max thruster result after feedback = {result_amp_e}")
        break

# if result_amp_e > max_thruster:
#     max_thruster = result_amp_e
