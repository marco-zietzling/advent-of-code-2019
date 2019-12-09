# advent of code 2019 - shared intcode computer / interpreter


class IntcodeComputer:
    """Simple intcode computer running a set of operations on defined input program"""

    # constructor for a new intcode computer
    def __init__(self, filename):
        self.filename = filename
        self.instructions = list()
        self.base_offset = 0
        self.instruction_pointer = 0

    def read_program(self):
        """read program instructions from input file"""

        print(f"load {self.filename}")
        with open(self.filename) as file:
            self.instructions = [int(i) for i in file.readline().split(",")]

    def get_parameter(self, mode: int, arg: int):
        # position mode
        if mode == 0:
            return int(self.instructions[arg])
        # immediate mode
        elif mode == 1:
            return int(arg)
        # relative mode
        elif mode == 2:
            return int(self.instructions[self.base_offset + arg])

    def run_program(self, phase_setting: int, input_signal: int):
        relative_base = 0
        phase_setting_used = False
        input_signal_used = False
        program_output = 9999

        while True:
            instruction = self.instructions[self.instruction_pointer]
            # print(f"instruction = {instruction}")

            instruction_str = str(instruction).zfill(5)
            # print(f"instruction string = {instruction_str}")

            opcode = int(instruction_str[3:])
            param1_mode = int(instruction_str[2])
            param2_mode = int(instruction_str[1])
            # print(f"opcode = {opcode}, p1mode = {param1_mode}, p2mode = {param2_mode}, p3mode = {param3_mode}")

            # halt (and return program output)
            if opcode == 99:
                return 99, program_output

            # addition
            elif opcode == 1:
                arg1 = self.get_parameter(param1_mode, self.instructions[self.instruction_pointer + 1])
                arg2 = self.get_parameter(param2_mode, self.instructions[self.instruction_pointer + 2])
                target_index = self.instructions[self.instruction_pointer + 3]
                self.instructions[target_index] = arg1 + arg2
                self.instruction_pointer += 4

            # multiplication
            elif opcode == 2:
                arg1 = self.get_parameter(param1_mode, self.instructions[self.instruction_pointer + 1])
                arg2 = self.get_parameter(param2_mode, self.instructions[self.instruction_pointer + 2])
                target_index = self.instructions[self.instruction_pointer + 3]
                self.instructions[target_index] = arg1 * arg2
                self.instruction_pointer += 4

            # read input and save at index
            elif opcode == 3:
                target_index = self.instructions[self.instruction_pointer + 1]
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

                self.instructions[target_index] = input_to_be_used
                # print(f"read input {program[target_index]} and stored it at position {target_index}")
                self.instruction_pointer += 2

            # output value at index
            elif opcode == 4:
                target_index = self.instructions[self.instruction_pointer + 1]
                program_output = self.instructions[target_index]
                self.instruction_pointer += 2
                # print(f"program output = {program[target_index]}")
                return 4, program_output

            # jump if true
            elif opcode == 5:
                arg1 = self.get_parameter(param1_mode, self.instructions[self.instruction_pointer + 1])
                arg2 = self.get_parameter(param2_mode, self.instructions[self.instruction_pointer + 2])
                if arg1 != 0:
                    self.instruction_pointer = arg2
                else:
                    self.instruction_pointer += 3

            # jump if false
            elif opcode == 6:
                arg1 = self.get_parameter(param1_mode, self.instructions[self.instruction_pointer + 1])
                arg2 = self.get_parameter(param2_mode, self.instructions[self.instruction_pointer + 2])

                if arg1 == 0:
                    self.instruction_pointer = arg2
                else:
                    self.instruction_pointer += 3

            # less than
            elif opcode == 7:
                arg1 = self.get_parameter(param1_mode, self.instructions[self.instruction_pointer + 1])
                arg2 = self.get_parameter(param2_mode, self.instructions[self.instruction_pointer + 2])
                target_index = self.instructions[self.instruction_pointer + 3]

                if arg1 < arg2:
                    self.instructions[target_index] = 1
                else:
                    self.instructions[target_index] = 0

                self.instruction_pointer += 4

            # equals
            elif opcode == 8:
                arg1 = self.get_parameter(param1_mode, self.instructions[self.instruction_pointer + 1])
                arg2 = self.get_parameter(param2_mode, self.instructions[self.instruction_pointer + 2])
                target_index = self.instructions[self.instruction_pointer + 3]

                if arg1 == arg2:
                    self.instructions[target_index] = 1
                else:
                    self.instructions[target_index] = 0

                self.instruction_pointer += 4

            else:
                print(f"program exception - unknown opcode = {opcode}")
                break
