import math
import os
from collections import defaultdict

print("advent of code 2019 - day 14")


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


def create_fuel(recipes: dict, target_amount_fuel: int):
    required_chems = defaultdict(int)
    required_chems["FUEL"] = target_amount_fuel
    work_queue = ["FUEL"]

    while work_queue:
        # print(f"current queue: {work_queue}")
        # print(f"current required chems: {required_chems}")
        current_product = work_queue.pop()

        for recipe in recipes.keys():
            if recipe[1] == current_product:
                factor = math.ceil(required_chems[current_product] / recipe[0])
                # print(f"Recipe required with factor {factor}: {recipe} <= {recipes[recipe]}")

                for ingredient in recipes[recipe]:
                    required_chems[ingredient[1]] += int(factor * ingredient[0])
                    if required_chems[current_product] > 0:
                        work_queue.append(ingredient[1])

                required_chems[current_product] -= factor * recipe[0]

    return required_chems['ORE']


# day 14 - part 1

# input_file = os.path.join(os.getcwd(), "sample1.txt") # 31 ORE for 1 FUEL
# input_file = os.path.join(os.getcwd(), "sample2.txt") # 165 ORE for 1 FUEL
# input_file = os.path.join(os.getcwd(), "sample3.txt")  # 13312 ORE for 1 FUEL
input_file = os.path.join(os.getcwd(), "input.txt")
recipes = read_recipes(input_file)
ores_required = create_fuel(recipes, 1)

# result: 220019
print(f"ORE required for 1 FUEL: {ores_required}")

# day 14 - part 2
trillion_ore = 1000000000000
low = trillion_ore // ores_required
high = trillion_ore - 1

while low <= high:
    mid = (low + high) // 2
    if low == mid:
        break

    ores_required = create_fuel(recipes, mid)
    if ores_required < trillion_ore:
        low = mid + 1
    else:
        high = mid - 1

# result = 5650230
print(f"Most FUEL that can be produced with 1 trillion ORE: {low}")
