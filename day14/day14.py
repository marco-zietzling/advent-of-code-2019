import math
import os
from collections import defaultdict

print("advent of code 2019 - day 14")

# day 14 - part 1

# input_file = os.path.join(os.getcwd(), "sample1.txt") # 31 ORE
# input_file = os.path.join(os.getcwd(), "sample2.txt") # 165 ORE
input_file = os.path.join(os.getcwd(), "sample3.txt") # 13312 ORE
# input_file = os.path.join(os.getcwd(), "input.txt")


def read_recipes(input_file: str):
    result = dict()

    with open(input_file) as file:
        lines = [line.strip() for line in file]
        for line in lines:
            product = line.split(" => ")[1]
            ingredients = line.split(" => ")[0].split(", ")

            amount, chem = product.split()
            product = (int(amount), chem)

            ingredients_list = []
            for ingredient in ingredients:
                amount, chem = ingredient.split()
                ingredients_list.append((int(amount), chem))

            result[product] = ingredients_list

    return result


recipes = read_recipes(input_file)
print(recipes)

required = defaultdict(int)
required["FUEL"] = 1
work_queue = ["FUEL"]

while work_queue:
    print(f"current queue: {work_queue}")
    print(f"current required chems: {required}")
    current_product = work_queue.pop()

    for recipe in recipes.keys():
        if recipe[1] == current_product:
            factor = math.ceil(required[current_product] / recipe[0])
            print(f"Recipe required with factor {factor}: {recipe} <= {recipes[recipe]}")

            for ingredient in recipes[recipe]:
                required[ingredient[1]] += int(factor * ingredient[0])
                if required[current_product] > 0:
                    work_queue.append(ingredient[1])

            required[current_product] -= factor * recipe[0]

# result: 220019
print(f"ORE required: {required['ORE']}")

