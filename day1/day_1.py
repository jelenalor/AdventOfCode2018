# DAY 1
with open("input.txt") as f:
    data = f.readlines()
    data = [int(i) for i in data]
# print(data)

# CHALLENGE 1
# result = 0
# for i in data:
#     result += i
# print(result)

# CHALLENGE 2
result = 0
list_of_sums = []
list_of_sums.append(result)
found = False
while not found:
    for i in data:
        result += i
        if result in list_of_sums:
            found = True
            # seen already
            print(result)
            break
        else:
            list_of_sums.append(result)
