print("advent of code 2019 - day 3")

with open("input.txt") as file:
    lines = [line.split(",") for line in file]

grid = [[' ' for x in range(-13000, 13000)] for y in range(-13000, 13000)]


def print_grid(grid):
    with open("result1.txt", mode="w") as file:
        file.write("\n".join([''.join(["{:1}".format(i) for i in row]) for row in grid]))
        # for y in range(len(grid)):
        #     for x in range(len(grid)):
        #         file.write("{:1}".format(grid[x][y]))
        #
        #     file.write("\n")


def process_wire(wire):
    x = 0
    y = 0
    grid[y][x] = "O"
    for action in wire:
        direction = action[:1]
        steps = int(action[1:])
        print(f"go {direction} {steps} steps")
        if direction == "R":
            for x in range(x + 1, x + steps, +1):
                grid[y][x] = "-"

            x = x + 1
        elif direction == "L":
            for x in range(x - 1, x - steps, -1):
                grid[y][x] = "-"

            x = x - 1
        elif direction == "U":
            for y in range(y + 1, y + steps, +1):
                grid[y][x] = "|"

            y = y + 1
        elif direction == "D":
            for y in range(y - 1, y - steps, -1):
                grid[y][x] = "|"

            y = y - 1
        else:
            print(f"unknown direction {direction}")

        grid[y][x] = "X"
        print(f"current coordinates {x} {y} and {grid[y][x]}")


process_wire(lines[0])
# process_wire(lines[1])

print_grid(grid)
