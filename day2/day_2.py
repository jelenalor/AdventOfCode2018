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
# print(checksum(data))


# PART 2
test = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]


def count_the_same(row1, row2):
    num = 0
    for i in range(len(row1)):
        if row1[i] == row2[i]:
            num += 1
    return num


def get_dict_count(data):
    dict_res = {}
    for i, row in enumerate(data):
        dict_res[i] = []
        for j in range(i+1, len(data)):
            row1 = data[i]
            row2 = data[j]
            num = count_the_same(row1, row2)
            dict_res[i].append(num)
    return dict_res


def find_pair(dict_res, test):
    k = 0
    len_ = len(test[0])-1
    for i in dict_res.keys():
        if len_ in dict_res[i]:
            k = i
            break
    v = 0
    for i, j in enumerate(dict_res[k]):
        if j == len_:
            v = i
    l = k+v+1
    pair = (test[k], test[l])
    return pair


def find_common(pair):
    common = ""
    for i in range(len(pair[0])):
        if pair[0][i] == pair[1][i]:
            common += pair[0][i]
    return common


def alg(data):
    dict_count = get_dict_count(data)
    pair = find_pair(dict_count, data)
    common = find_common(pair)
    return common, pair

print(alg(data))





