
# input - polymers:
# type -> the same letter
# polarity -> the same case
# reaction -> the same type but not the same polarity

# test case:
# abBA -> [bB - destroys] -> aA -? [aA - destroys]
#

# reacts -> aA or Aa   Not aa AA

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


current_index = 1
while current_index < len(text):

    # if deleted check again the same index
    round = True
    while round:
        # extract current and future value
        t1 = text[current_index]
        t2 = text[current_index - 1]
        #  check current_index and future_index
        # print(current_index)
        # print("t1, t2 - %s - %s" % (t1, t2))
        if isType(t1, t2) and not isPolarity(t1, t2):
            # print("deleted %s %s" % (text[current_index], text[current_index - 1]))
            del text[current_index]
            del text[current_index - 1]
            if current_index > 1:
                current_index -= 1
            else:
                current_index = 1
            # print("upd text len", len(text))
            # print("upd text", text[:30])
            continue
        else:
            round = False
            current_index += 1
            break

print(len(text)-1)





