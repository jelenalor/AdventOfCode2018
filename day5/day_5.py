import string

# input - polymers:
# type -> the same letter
# polarity -> the same case
# reaction -> the same type but not the same polarity

# test case:
# abBA -> [bB - destroys] -> aA -? [aA - destroys]
#

# reacts -> aA or Aa   Not aa AA
test = list('dabAcCaCBAcCcaDA')


with open("input.txt") as f:
    data = f.readlines()
    text = list("".join(data))


def isPolarity(t1, t2):
    # both are upper
    if t1.isupper() and t2.isupper():
        return True
    # both are lower
    elif t1.islower() and t2.islower():
        return True
    else:
        return False


def isType(t1, t2):
    # both lower are equal
    if t1.lower() == t2.lower():
        return True
    else:
        return False


def my_solution(text):
    # print(text)
    my_text = text
    current_index = 1
    while current_index < len(my_text):
        # print(current_index)
        # if deleted check again the same index
        round = True
        while round:
            # extract current and future value
            t1 = my_text[current_index]
            t2 = my_text[current_index - 1]
            #  check current_index and future_index
            if isType(t1, t2) and not isPolarity(t1, t2):
                del my_text[current_index]
                del my_text[current_index - 1]
                if current_index > 1:
                    current_index -= 1
                else:
                    current_index = 1
                continue
            else:
                round = False
                current_index += 1
                break

    return len(my_text)-1


def my_solution2(text):
    # for each letter in alphabet
    # remove the letter and capital letter
    # apply my_solution to the 'new'text
    # store solutions
    my_dict = {}
    for i in string.ascii_lowercase:
        my_text = text
        i_c = i.capitalize()
        # print("i", i)
        # print("i_c", i_c)
        if i in my_text:
            my_text = [l for l in my_text if l != i]
        if i_c in my_text:
            my_text = [l for l in my_text if l != i_c]
        # print("text", my_text)
        result = my_solution(my_text)
        my_dict[i] = result
    # print(my_dict)
    result = 100000
    for j in my_dict.keys():
        if my_dict[j] < result:
            result = my_dict[j]

    return result

print(my_solution2(text))


