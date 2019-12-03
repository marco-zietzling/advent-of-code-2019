from collections import defaultdict

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

min_distance = min(calculate_manhatten_distance(crossing) for crossing in crossings)

# result = 1195
print(f"minimum manhattan distance = {min_distance}")


# day 3 - part 2


def calculate_distance_for_crossings(wire, crossings):
    x = 0
    y = 0
    distance = 0
    crossing_distances = defaultdict(int)

    for action in wire:
        direction = action[:1]
        steps = int(action[1:])

        if direction == "R":
            for x in range(x + 1, x + steps + 1, +1):
                distance += 1
                if (x, y) in crossings:
                    crossing_distances[(x, y)] = distance
        elif direction == "L":
            for x in range(x - 1, x - steps - 1, -1):
                distance += 1
                if (x, y) in crossings:
                    crossing_distances[(x, y)] = distance
        elif direction == "U":
            for y in range(y + 1, y + steps + 1, +1):
                distance += 1
                if (x, y) in crossings:
                    crossing_distances[(x, y)] = distance
        elif direction == "D":
            for y in range(y - 1, y - steps - 1, -1):
                distance += 1
                if (x, y) in crossings:
                    crossing_distances[(x, y)] = distance
        else:
            print(f"unknown direction {direction}")

    return crossing_distances


crossing_distances1 = calculate_distance_for_crossings(lines[0], crossings)
crossing_distances2 = calculate_distance_for_crossings(lines[1], crossings)
min_crossing_distance = min(crossing_distances1[crossing] + crossing_distances2[crossing] for crossing in crossings)

# result = 91518
print(f"minimum crossing distance = {min_crossing_distance}")
