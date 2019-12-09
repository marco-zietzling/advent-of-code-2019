import intcode.intcode_computer as comp
import os

print("advent of code 2019 - day 9")

# day 9 - part 1
# input_program = comp.read_program(os.path.join(os.getcwd(), "input.txt"))

computer = comp.IntcodeComputer(os.path.join(os.getcwd(), "input.txt"))
computer.read_program()

print(computer.instructions)
