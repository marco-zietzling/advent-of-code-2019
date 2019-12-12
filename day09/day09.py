import intcode.intcode_computer as comp
import os

print("advent of code 2019 - day 9")

# day 9 - part 1
input_file = os.path.join(os.getcwd(), "input.txt")

computer = comp.IntcodeComputer("part1", input_file)
computer.provide_arguments([1])
computer.execute()
result = computer.consume_output()

# result = 2351176124
print(f"result = {result}")

# day 9 - part 2
computer = comp.IntcodeComputer("part2", input_file)
computer.provide_arguments([2])
computer.execute()
result = computer.consume_output()

# result = 73110
print(f"result = {result}")
