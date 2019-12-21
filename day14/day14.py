import os

print("advent of code 2019 - day 14")

# day 14 - part 1
input_file = os.path.join(os.getcwd(), "input.txt")
with open(input_file) as file:
    for line in file:
        ingredients, result = line.split(" => ")
        print(ingredients)
        print(result)
