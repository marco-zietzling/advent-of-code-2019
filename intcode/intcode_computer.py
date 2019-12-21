# advent of code 2019 - shared intcode computer / interpreter


class IntcodeComputer:
    """Simple intcode computer running a set of operations on defined input program"""

    def __init__(self, name: str, filename: str):
        """constructor for a new intcode computer with provided name and input file"""
        self.name = name
        self.instructions = []
        self.instruction_pointer = 0
        self.relative_base = 0
        self.output = []
        self.arguments = []
        self.argument_pointer = 0

        # print(f"load {filename}")
        with open(filename) as file:
            self.instructions = [int(i) for i in file.readline().split(",")] + [0] * 1000

    def get_interpreted_param(self, mode: int, arg: int):
        # position mode
        if mode == 0:
            return int(self.instructions[arg])
        # immediate mode
        elif mode == 1:
            return int(arg)
        # relative mode
        elif mode == 2:
            return int(self.instructions[self.relative_base + arg])

    def get_literal_param(self, mode: int, arg: int):
        # position mode
        if mode == 0:
            return int(arg)
        # immediate mode
        elif mode == 1:
            return int(arg)
        # relative mode
        elif mode == 2:
            return int(self.relative_base + arg)

    def provide_arguments(self, arguments: list):
        self.arguments.extend(arguments)

    def consume_output(self):
        result = self.output.copy()
        self.output.clear()
        return result

    def execute(self):
        while True:
            instruction = self.instructions[self.instruction_pointer]
            instruction_str = str(instruction).zfill(5)

            opcode = int(instruction_str[3:])
            param1_mode = int(instruction_str[2])
            param2_mode = int(instruction_str[1])
            param3_mode = int(instruction_str[0])
            # print(f"opcode = {opcode}, p1mode = {param1_mode}, p2mode = {param2_mode}, p3mode = {param3_mode}")

            # halt (and return exit code)
            if opcode == 99:
                return opcode

            # addition
            elif opcode == 1:
                arg1 = self.get_interpreted_param(param1_mode, self.instructions[self.instruction_pointer + 1])
                arg2 = self.get_interpreted_param(param2_mode, self.instructions[self.instruction_pointer + 2])
                arg3 = self.get_literal_param(param3_mode, self.instructions[self.instruction_pointer + 3])
                self.instructions[arg3] = arg1 + arg2
                self.instruction_pointer += 4

            # multiplication
            elif opcode == 2:
                arg1 = self.get_interpreted_param(param1_mode, self.instructions[self.instruction_pointer + 1])
                arg2 = self.get_interpreted_param(param2_mode, self.instructions[self.instruction_pointer + 2])
                arg3 = self.get_literal_param(param3_mode, self.instructions[self.instruction_pointer + 3])
                self.instructions[arg3] = arg1 * arg2
                self.instruction_pointer += 4

            # read input and save at index, in case of not enough input values, halt (and return exit code)
            elif opcode == 3:
                # check if we have enough input arguments, otherwise suspend processing
                if self.argument_pointer >= len(self.arguments):
                    return opcode

                arg1 = self.get_literal_param(param1_mode, self.instructions[self.instruction_pointer + 1])
                self.instructions[arg1] = self.arguments[self.argument_pointer]
                self.argument_pointer += 1
                self.instruction_pointer += 2

            # output value at index
            elif opcode == 4:
                arg1 = self.get_interpreted_param(param1_mode, self.instructions[self.instruction_pointer + 1])
                self.output.append(arg1)
                self.instruction_pointer += 2

            # jump if true
            elif opcode == 5:
                arg1 = self.get_interpreted_param(param1_mode, self.instructions[self.instruction_pointer + 1])
                arg2 = self.get_interpreted_param(param2_mode, self.instructions[self.instruction_pointer + 2])
                if arg1 != 0:
                    self.instruction_pointer = arg2
                else:
                    self.instruction_pointer += 3

            # jump if false
            elif opcode == 6:
                arg1 = self.get_interpreted_param(param1_mode, self.instructions[self.instruction_pointer + 1])
                arg2 = self.get_interpreted_param(param2_mode, self.instructions[self.instruction_pointer + 2])

                if arg1 == 0:
                    self.instruction_pointer = arg2
                else:
                    self.instruction_pointer += 3

            # less than
            elif opcode == 7:
                arg1 = self.get_interpreted_param(param1_mode, self.instructions[self.instruction_pointer + 1])
                arg2 = self.get_interpreted_param(param2_mode, self.instructions[self.instruction_pointer + 2])
                arg3 = self.get_literal_param(param3_mode, self.instructions[self.instruction_pointer + 3])

                if arg1 < arg2:
                    self.instructions[arg3] = 1
                else:
                    self.instructions[arg3] = 0

                self.instruction_pointer += 4

            # equals
            elif opcode == 8:
                arg1 = self.get_interpreted_param(param1_mode, self.instructions[self.instruction_pointer + 1])
                arg2 = self.get_interpreted_param(param2_mode, self.instructions[self.instruction_pointer + 2])
                arg3 = self.get_literal_param(param3_mode, self.instructions[self.instruction_pointer + 3])

                if arg1 == arg2:
                    self.instructions[arg3] = 1
                else:
                    self.instructions[arg3] = 0

                self.instruction_pointer += 4

            # adjust relative base
            elif opcode == 9:
                arg1 = self.get_interpreted_param(param1_mode, self.instructions[self.instruction_pointer + 1])
                self.relative_base += arg1
                self.instruction_pointer += 2

            else:
                raise NameError(f"unknown opcode: {opcode}")
