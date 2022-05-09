#!/usr/bin/python3
"""
Find the island perimeter.
Note: I have done this before, this version is beautified.
The grid contains island with no lake, edges are coasts,
coasts may attach to the borders.
rowLen: the length of row, should be less than 100
colLen: the length of column, should be less than 100
xCoast: length count of the x direction facing coast
return: the island perimeter
"""


def island_perimeter(grid):
    rowLen = len(grid)
    colLen = len(grid[0])
    westCoast = eastCoast = northCoast = southCoast = 0
    if grid is None:
        return 0
    for i in range(rowLen):
        for j in range(colLen):
            if grid[i][j] == 1 and (i - 1 < 0 or grid[i - 1][j] == 0):
                westCoast += 1
            if grid[i][j] == 1 and (i + 1 >= rowLen or grid[i + 1][j] == 0):
                eastCoast += 1
            if grid[i][j] == 1 and (j - 1 < 0 or grid[i][j - 1] == 0):
                northCoast += 1
            if grid[i][j] == 1 and (j + 1 >= colLen or grid[i][j + 1] == 0):
                southCoast += 1
    perimeter = westCoast + eastCoast + northCoast + southCoast
    return perimeter
