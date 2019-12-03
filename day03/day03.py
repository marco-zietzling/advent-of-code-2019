print("advent of code 2019 - day 3")

# day 1 - part 1

with open("input.txt") as file:
    lines = [line.split(",") for line in file]


def calculate_manhatten_distance(position):
    return abs(position[0]) + abs(position[1])


def process_wire(wire):
    x = 0
    y = 0
    wire_positions = set()

    for action in wire:
        direction = action[:1]
        steps = int(action[1:])
        # print(f"go {direction} {steps} steps")

        if direction == "R":
            for x in range(x + 1, x + steps + 1, +1):
                wire_positions.add((x, y))
        elif direction == "L":
            for x in range(x - 1, x - steps - 1, -1):
                wire_positions.add((x, y))
        elif direction == "U":
            for y in range(y + 1, y + steps + 1, +1):
                wire_positions.add((x, y))
        elif direction == "D":
            for y in range(y - 1, y - steps - 1, -1):
                wire_positions.add((x, y))
        else:
            print(f"unknown direction {direction}")

        # print(f"current coordinates {x} {y}")

    return wire_positions


wire1_positions = process_wire(lines[0])
wire2_positions = process_wire(lines[1])

crossings = wire1_positions.intersection(wire2_positions)

min_distance = 99999
for crossing in crossings:
    distance = calculate_manhatten_distance(crossing)
    if distance < min_distance:
        min_distance = distance

# result = 1195
print(f"minimum manhattan distance = {min_distance}")

# day 3 - part 2

