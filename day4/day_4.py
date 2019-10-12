import numpy as np
import pandas as pd

""" Input """
with open("input.txt") as f:
    data = f.readlines()
    data = [str(i).strip() for i in data]

""" Test """
test = ['[1518-11-01 00:00] Guard #10 begins shift',
        '[1518-11-01 00:25] wakes up', '[1518-11-01 00:30] falls asleep',
        '[1518-11-01 00:55] wakes up', '[1518-11-01 23:58] Guard #99 begins shift',
        '[1518-11-02 00:40] falls asleep', '[1518-11-02 00:50] wakes up',
        '[1518-11-03 00:05] Guard #10 begins shift', '[1518-11-03 00:24] falls asleep',
        '[1518-11-03 00:29] wakes up', '[1518-11-04 00:02] Guard #99 begins shift',
        '[1518-11-04 00:36] falls asleep', '[1518-11-04 00:46] wakes up',
        '[1518-11-05 00:03] Guard #99 begins shift', '[1518-11-05 00:45] falls asleep',
        '[1518-11-05 00:55] wakes up]', '[1518-11-01 00:05] falls asleep']



prev_guard = ""
def extract_guard(row):
    global prev_guard
    if "Guard" in row:
        g = row.split()[1]
        prev_guard = g
        return g
    else:
        return prev_guard

def my_solution(test):
    # Cleaning and sorting
    my_dict = {"year": [], "month": [], "day": [], "hour": [], "minute": [], "text": []}
    for i in test:
        date = i.split("]")[0].replace("[", "")
        text = i.split("]")[1][1:]

        my_dict["year"].append(date.split("-")[0])
        my_dict["month"].append(date.split("-")[1])
        my_dict["day"].append(date.split("-")[2].split()[0])
        my_dict["hour"].append(date.split("-")[2].split()[1].split(":")[0])
        my_dict["minute"].append(date.split("-")[2].split()[1].split(":")[1])
        my_dict["text"].append(text)

    df = pd.DataFrame(my_dict)
    df = df.sort_values(by=["year", "month", "day", "hour", "minute"])

    # Extract guard number and keep in a separate column
    df["guard"] = df["text"].apply(extract_guard)

    # Keep in numpy 2D array minutes of sleep and in separate array the guards in order
    list_of_guards = []
    my_np = []

    guard = ""
    start = 0
    for i in range(df.shape[0]):
        if "asleep" in df.iloc[i]["text"]:
            guard = df.iloc[i]["guard"]
            start = df.iloc[i]["minute"]
        elif "wakes" in df.iloc[i]["text"]:
            end = df.iloc[i]["minute"]
            my_range = range(int(start), int(end))
            list_of_guards.append(guard)
            my_row = [0]*60
            for i in my_range:
                my_row[i] = 1
            my_np.append(my_row)

    my_np = np.array(my_np)
    list_of_guards = np.array(list_of_guards)

    # to find the guard that sleeps the most
    most = 0
    most_guard = ""
    for g in set(list_of_guards):
        my_list = my_np[list_of_guards == g]
        my_list = my_list.flatten()
        count = sum(my_list)
        if count > most:
            most = count
            most_guard = g

    # to find most minute
    dff = my_np[list_of_guards == most_guard]
    most_min = np.argmax(dff.sum(axis=0))

    result = int(most_guard[1:]) * most_min

    return most_guard, most_min, result


g, m, r = my_solution(data)
print(g, m, r)