""" Input """
with open("input.txt") as f:
    data = f.readlines()
    data = [str(i).strip() for i in data]

""" Support Functions """


def count(row):
    seen = {}
    for i in list(row):
        if i in seen.keys():
            seen[i] += 1
        else:
            seen[i] = 1
    return seen


def summary(seen):
    count_2, count_3 = 0, 0
    if 2 in seen.values():
        count_2 = 1
    if 3 in seen.values():
        count_3 = 1
    return count_2, count_3


def checksum(data):
    count2 = 0
    count3 = 0
    for row in data:
        seen = count(row)
        c2, c3 = summary(seen)
        count2 += c2
        count3 += c3
    return count2*count3

# test = ['abcdef', "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
print(checksum(data))


