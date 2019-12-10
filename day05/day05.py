import intcode.intcode_computer as comp
import os

print("advent of code 2019 - day 5")

# day 5 - part 1
input_file = os.path.join(os.getcwd(), "input.txt")

computer = comp.IntcodeComputer("Day 5", input_file)
result = computer.run_program([1])
print(f"result for part 1 = {result}")
# result = 7286649

# day 5 - part 2
computer = comp.IntcodeComputer("Day 5", input_file)
result = computer.run_program([5])
print(f"result for part 2 = {result}")
# result = 15724522
