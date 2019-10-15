import string
import numpy as np

data = []
with open("input.txt") as f:
    temp = f.readlines()
    for i in temp:
        data.append(tuple([int(j.replace(",", "")) for j in i.split()]))

test = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]
# print(test)


def find_size(test):
    dim_col = 0
    dim_row = 0
    for i in range(len(test)):
        if test[i][0] > dim_col:
            dim_col = test[i][0]
        if test[i][1] > dim_row:
            dim_row = test[i][1]
    return dim_col, dim_row


def manhattanDistance(point1, point2):
    dist = np.abs(point1[0] - point2[0]) + np.abs(point1[1] - point2[1])
    return dist


def populateGrid(grid, test):
    # for each point calculate distance and choose the closest one
    # if actual point then capital letter
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            point = (col, row)
            # find lowest dist
            lowest_point = 0
            lowest_dist = 1000
            for ind, k in enumerate(test):
                dist = manhattanDistance(point, k)
                if dist < lowest_dist:
                    lowest_dist = dist
                    lowest_point = ind+1
                elif dist == lowest_dist:
                    lowest_point = 0

            grid[point[1], point[0]] = lowest_point
    return grid


def my_solution(test):
    dim_col, dim_row = find_size(test)
    grid = np.zeros((dim_row+1, dim_col+1))
    grid = populateGrid(grid, test)
    items = set(range(1, len(test)+1))
    border_items = set()
    for i in range(grid.shape[0]):
        border_items.add(grid[i, 0])
        border_items.add(grid[i, grid.shape[1]-1])
    for j in range(grid.shape[1]):
        border_items.add(grid[0, j])
        border_items.add(grid[grid.shape[0]-1, j])

    not_infinite = items - border_items
    v, c = np.unique(grid, return_counts=True)
    result = 0
    for i in not_infinite:
        if c[i] > result:
            result = c[i]

    return result


def populateGrid2(grid, test):
    # for each point calculate distance and sum all distances to all other points
    # if actual point then capital letter
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            point = (col, row)
            # find lowest dist
            total_dist = 0
            for k in test:
                dist = manhattanDistance(point, k)
                total_dist += dist
            if total_dist < 10000:
                grid[point[1], point[0]] = 1
    return grid


def my_solution2(test):
    dim_col, dim_row = find_size(test)
    grid = np.zeros((dim_row + 1, dim_col + 1))
    grid = populateGrid2(grid, test)
    v, c = np.unique(grid, return_counts=True)
    return v, c


print(my_solution2(data))