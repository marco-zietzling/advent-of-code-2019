import os
import intcode.intcode_computer as comp

print("advent of code 2019 - day 13")

# day 13 - part 1
input_file = os.path.join(os.getcwd(), "input.txt")
computer = comp.IntcodeComputer("Arcade", input_file)
computer.execute()
output = computer.consume_output()

block_tile_counter = 0

for pos in range(0, len(output), 3):
    x = output[pos]
    y = output[pos + 1]
    tile_type = output[pos + 2]

    if tile_type == 2:
        block_tile_counter += 1

# result = 284
print(f"number block tiles = {block_tile_counter}")

# day 13 - part 2
computer = comp.IntcodeComputer("Arcade", input_file)
computer.instructions[0] = 2

joystick = 0
segment_display = 0
