import numpy as np

""" Input """
with open("input.txt") as f:
    data = f.readlines()
    data = [str(i).strip() for i in data]

""" Test """
test = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]


my_dict = {}
for i in data:
    size = (int(i.split()[3].split("x")[0]), int(i.split()[3].split("x")[1]))
    position = (int(i.split()[2].split(",")[0]), int(i.split()[2].split(",")[1][:-1]))
    col_range = range(position[0], (position[0]+size[0]))
    row_range = range(position[1], (position[1]+size[1]))
    item = int(i.split()[0][1:])

    for c in col_range:
        for r in row_range:
            my_key = tuple([c, r])
            if my_key not in my_dict:
                my_dict[my_key] = []

            my_dict[my_key].append(item)

my_list = []
for k in my_dict.keys():
    if len(my_dict[k]) > 1:
        for v in my_dict[k]:
            my_list.append(v)

my_list = set(my_list)


all_values = set([])
for i in my_dict.values():
    for j in i:
        all_values.add(j)

print(all_values-my_list)



