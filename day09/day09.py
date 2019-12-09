import intcode.intcode_computer as comp
import os

print("advent of code 2019 - day 9")

# day 9 - part 1

computer = comp.IntcodeComputer("part1", "input.txt")
result = computer.run_program([1])

# result = 2351176124
print(f"result = {result}")

# day 9 - part 2
computer = comp.IntcodeComputer("part2", "input.txt")
result = computer.run_program([2])

# result = 73110
print(f"result = {result}")
