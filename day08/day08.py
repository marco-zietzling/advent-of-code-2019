print("advent of code 2019 - day 8")

# day 8 - part 1

with open("input.txt") as file:
    lines = [line.strip() for line in file]

password = lines[0]
image_width = 25
image_height = 6
layer_length = image_height * image_width
number_of_layers = int(len(password) / layer_length)
layer_dict = dict()

print(f"input length = {len(password)} equals {number_of_layers} layers")

for current_layer_counter in range(number_of_layers):
    current_layer_content = password[
                            current_layer_counter * layer_length:current_layer_counter * layer_length + layer_length]
    # print(f"layer {current_layer_counter} = {current_layer_content}")
    num_0 = current_layer_content.count("0")
    num_1 = current_layer_content.count("1")
    num_2 = current_layer_content.count("2")
    layer_dict[current_layer_counter] = (num_0, num_1, num_2)
    # print(f"layer {current_layer_counter} has {num_0} 0s, {num_1} 1s, {num_2} 2s")

target_layer = min(layer_dict.items(), key=lambda x: x[1][0])

# result = 1965
print(f"target layer = {target_layer[1]} with result = {target_layer[1][1] * target_layer[1][2]}")

# day 8 - part 2
canvas = [["2" for x in range(image_width)] for y in range(image_height)]

for current_layer_counter in range(number_of_layers):
    current_layer_content = password[
                            current_layer_counter * layer_length:current_layer_counter * layer_length + layer_length]

    for x in range(image_width):
        for y in range(image_height):
            current_pixel = current_layer_content[y * image_width + x]
            if canvas[y][x] == "2":
                canvas[y][x] = current_pixel

# cleanup canvas and produce nicer looking "pixels"
for x in range(image_width):
    for y in range(image_height):
        current_pixel = current_layer_content[y * image_width + x]
        if canvas[y][x] == "0":
            canvas[y][x] = " "
        elif canvas[y][x] == "1":
            canvas[y][x] = "*"

with open("result.txt", mode="w") as file:
    file.write("\n".join([''.join(["{:2}".format(i) for i in row]) for row in canvas]))

# result = GZKJY
