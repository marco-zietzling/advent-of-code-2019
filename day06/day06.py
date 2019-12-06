print("advent of code 2019 - day 6")


# day 6 - part 1

def count_recursive_orbits(current_set, orbit_sets):
    # print(f"recursive counter for set {current_set}")
    counter = 1
    (x, y) = current_set
    for subset in [(a, b) for (a, b) in orbit_sets if x == b]:
        counter += count_recursive_orbits(subset, orbit_sets)
    return counter


orbit_sets = set()

with open("input.txt") as file:
    lines = [line.strip() for line in file]
    for line in lines:
        (center, in_orbit) = line.split(")")
        orbit_sets.add((center, in_orbit))

print(orbit_sets)

orbit_counter = 0
for current_set in orbit_sets:
    # print(f"current set {current_set}")
    orbit_counter += count_recursive_orbits(current_set, orbit_sets)

# result = 295936
print(f"total orbit counter = {orbit_counter}")

# day 6 - part 2
