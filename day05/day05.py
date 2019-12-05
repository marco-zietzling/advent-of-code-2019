print("advent of code 2019 - day 5")


def read_input():
    with open("input.txt") as file:
        for line in file:
            return [int(i) for i in line.split(",")]


def run_program(input):
    current_index = 0

    while True:
        opcode = input[current_index]

        # terminate
        if opcode == 99:
            # print("program terminated - value at position '0'=" + str(input[0]))
            return input[0]

        # addition
        elif opcode == 1:
            index1 = input[current_index + 1]
            index2 = input[current_index + 2]
            index_target = input[current_index + 3]
            input[index_target] = input[index1] + input[index2]
            current_index = current_index + 4

        # multiplication
        elif opcode == 2:
            index1 = input[current_index + 1]
            index2 = input[current_index + 2]
            index_target = input[current_index + 3]
            input[index_target] = input[index1] * input[index2]
            current_index = current_index + 4

        else:
            print(f"program exception - unknown opcode {opcode}")
            break
