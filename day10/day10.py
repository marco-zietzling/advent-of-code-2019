import os
import math

print("advent of code 2019 - day 10")

# day 10 - part 1
input_file = os.path.join(os.getcwd(), "input.txt")


class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Asteroid (x={self.x}, y={self.y})"

    def calculate_angle_to(self, asteroid):
        return math.atan2(asteroid.y - self.y, asteroid.x - self.x)


asteroids = list()
asteroid_visible = dict()

with open(input_file) as file:
    y = 0
    for line in file:
        x = 0
        for char in line:
            if char == "#":
                asteroids.append(Asteroid(x, y))
            x += 1
        y += 1

print(f"total number of asteroids = {len(asteroids)}")

for candidate_asteroid in asteroids:
    others_visible = set()
    for other_asteroid in asteroids:
        if other_asteroid != candidate_asteroid:
            angle = round(candidate_asteroid.calculate_angle_to(other_asteroid), 8)
            others_visible.add(angle)

    # store result of visible other asteroids for current candidate
    asteroid_visible[candidate_asteroid] = len(others_visible)

    # print(f"other asteroids visible from current asteroids = {len(current_others_visible)}")

# result = 340
(target_asteroid, count) = max(asteroid_visible.items(), key=lambda x: x[1])
print(f"target asteroid = {target_asteroid} sees {count} other asteroids")

# day 10 - part 2
# asteroids_by_angle = dict()
#
# for other_asteroid in asteroids:
#     if other_asteroid != target_asteroid:
#         angle = round(target_asteroid.calculate_angle_to(other_asteroid), 8)
#         asteroids_by_angle[angle].append(other_asteroid)
#
# print(asteroids_by_angle)
