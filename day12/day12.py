import os

print("advent of code 2019 - day 12")


# day 12 - part 1
class Moon(object):
    def __init__(self, name: str, x: int, y: int, z: int):
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.velocity_x = 0
        self.velocity_y = 0
        self.velocity_z = 0

    def __eq__(self, other):
        if isinstance(other, Moon):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return False


input_file = os.path.join(os.getcwd(), "input.txt")
moons = []
names = ["Io", "Europa", "Ganymede", "Callisto"]


def read_input():
    current_name = 0
    moons = []
    with open(input_file) as file:
        for line in file:
            coords = [x.strip() for x in line.replace("<", "").replace(">", "").split(",")]
            x = int(coords[0].split("=")[1])
            y = int(coords[1].split("=")[1])
            z = int(coords[2].split("=")[1])
            moons.append(Moon(names[current_name], x, y, z))
            current_name += 1

    return moons


def calculate_velocity(a: int, b: int):
    if a == b:
        return 0
    elif a < b:
        return 1
    else:
        return -1


def calculate_potential_energy(moon: Moon):
    return abs(moon.x) + abs(moon.y) + abs(moon.z)


def calculate_kinetic_energy(moon: Moon):
    return abs(moon.velocity_x) + abs(moon.velocity_y) + abs(moon.velocity_z)


def execute_step(moons):
    # apply gravity
    for moon_a in moons:
        for moon_b in moons:
            if moon_a != moon_b:
                moon_a.velocity_x += calculate_velocity(moon_a.x, moon_b.x)
                moon_a.velocity_y += calculate_velocity(moon_a.y, moon_b.y)
                moon_a.velocity_z += calculate_velocity(moon_a.z, moon_b.z)

    # apply velocity
    for moon in moons:
        moon.x += moon.velocity_x
        moon.y += moon.velocity_y
        moon.z += moon.velocity_z


# for moon in moons:
#     print(f"{moon.name} coords = ({moon.x}, {moon.y}, {moon.z}) and "
#           f"velocity = ({moon.velocity_x}, {moon.velocity_y}, {moon.velocity_z})")

moons = read_input()
for step in range(1000):
    execute_step(moons)

for moon in moons:
    print(f"{moon.name} coords = ({moon.x}, {moon.y}, {moon.z}) and "
          f"velocity = ({moon.velocity_x}, {moon.velocity_y}, {moon.velocity_z})")

total_energy = 0
for moon in moons:
    total_energy += calculate_potential_energy(moon) * calculate_kinetic_energy(moon)

# result = 14809
print(f"total energy = {total_energy}")

# day 12 - part 2
moons = read_input()
original_moons = read_input()
current_step = 0

while True:
    execute_step(moons)
    current_step += 1
    if current_step % 10000 == 0:
        print(f"current step: {current_step}")

    if moons[0] == original_moons[0] and \
            moons[1] == original_moons[1] and \
            moons[2] == original_moons[2] and \
            moons[3] == original_moons[3]:
        break

print(f"identical state found after {current_step} steps")
