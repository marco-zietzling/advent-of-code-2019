print("advent of code 2019 - day 5")


# day 5 - part 1

def read_program():
    with open("input.txt") as file:
        for line in file:
            return [int(i) for i in line.split(",")]


def get_parameter(mode, program, param):
    # position mode
    if mode == 0:
        return int(program[param])
    # immediate mode
    elif mode == 1:
        return int(param)


def run_program(program):
    index = 0

    while True:
        instruction = program[index]
        # print(f"instruction = {instruction}")

        instruction_str = str(instruction).zfill(5)
        # print(f"instruction string = {instruction_str}")

        opcode = int(instruction_str[3:])
        param1_mode = int(instruction_str[2])
        param2_mode = int(instruction_str[1])
        # print(f"opcode = {opcode}, p1mode = {param1_mode}, p2mode = {param2_mode}, p3mode = {param3_mode}")

        # terminate
        if opcode == 99:
            # print("program terminated - value at position '0'=" + str(input[0]))
            return program[0]

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
            user_input = input("Enter your input: ")
            print(f"user input = {user_input}")
            program[target_index] = user_input
            print(f"read input {program[target_index]} and stored it at position {target_index}")
            index = index + 2

        # output value at index
        elif opcode == 4:
            target_index = program[index + 1]
            index = index + 2
            print(f"program output = {program[target_index]}")

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
            print(f"program exception - unknown opcode {opcode}")
            break


print(f"input for part1 = 1")
program = read_program()
run_program(program)
# result = 7286649

# day 5 - part 2

print(f"input for part1 = 5")
program = read_program()
run_program(program)
# result = 15724522
