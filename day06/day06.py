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

you_to_com = dict()
san_to_com = dict()


def find_centers(in_orbit, orbit_sets, current_step, orbit_center_steps):
    centers = [a for (a, b) in orbit_sets if in_orbit == b]
    for center in centers:
        orbit_center_steps[center] = current_step
        find_centers(center, orbit_sets, current_step + 1, orbit_center_steps)


find_centers("YOU", orbit_sets, 0, you_to_com)
find_centers("SAN", orbit_sets, 0, san_to_com)

print(f"steps YOU to COM = {len(you_to_com)}")
print(f"steps SAN to COM = {len(san_to_com)}")

common_centers = you_to_com.keys() & san_to_com.keys()

min_center_distance = 9999
min_center = "XXX"
for common_center in common_centers:
    current_center_distance = you_to_com[common_center]
    if current_center_distance < min_center_distance:
        min_center_distance = current_center_distance
        min_center = common_center

# result = 457
print(f"earliest common orbit center = {min_center}")
print(f"steps to earliest common orbit center = {you_to_com[min_center] + san_to_com[min_center]}")
