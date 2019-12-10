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
        return f"(x={self.x}, y={self.y})"

    def calculate_angle_to_point(self, asteroid):
        return math.atan2(asteroid.y - self.y, asteroid.x - self.x)

    # def calculate_angle_to_point(self, x: int, y: int):
    #     return math.atan2(y - self.y, x - self.x)


asteroids = list()

with open(input_file) as file:
    y = 0
    for line in file:
        x = 0
        for char in line:
            if char == "#":
                asteroids.append(Asteroid(x, y))
            x += 1
        y += 1

print(asteroids[0].calculate_angle_to_point(asteroids[20]))

for asteroid in asteroids:
    pass

# grid = [["" for x in range(42)] for y in range(42)]

# with open("result.txt", mode="w") as file:
#     file.write("\n".join([''.join(["{:2}".format(i) for i in row]) for row in grid]))
