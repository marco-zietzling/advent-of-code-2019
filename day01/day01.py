import math

print("advent of code 2019 - day 1")


# day 1 - part 1

def fuel_requirements_for_mass(mass):
    return math.floor(mass / 3) - 2


fuel_counter = 0.0
with open("input.txt") as file:
    for line in file:
        fuel_counter += fuel_requirements_for_mass(int(line))

# result = 3515171
print("part 1: " + str(int(fuel_counter)))


# day 1 - part 2

def total_fuel_requirements(mass):
    result = fuel_requirements_for_mass(mass)

    if result <= 0:
        return 0
    else:
        result += total_fuel_requirements(result)
        return result


fuel_counter = 0.0
with open("input.txt") as file:
    for line in file:
        fuel_counter += total_fuel_requirements(int(line))

# result = 5269882
print("part 2: " + str(int(fuel_counter)))
