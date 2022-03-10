#!/usr/bin/python3
"""
0-rain - input 'walls' is list of non-negative ints, 0s represent grounds,
other numbers represent heights of solid walls/dams. wall_i stores indices
of wall locations, wall_h stores wall tops to water level distances starting
from dry grounds. Return total amount of water to fill between the walls.
"""
import copy


def rain(walls):
    if walls is None:
        return 0
    wall_i = []
    wall_h = []
    water_sum = 0
    for i in range(len(walls)):
        if walls[i] > 0:
            wall_i.append(i)
            wall_h.append(walls[i])
    while len(wall_h) > 1:
        for i in range(len(wall_i) - 1):
            water_sum += wall_i[i + 1] - wall_i[i] - 1
        """water level to wall tops is going up"""
        wall_h = list((lambda x: x - 1)(x) for x in wall_h)
        """delete list elements, backward iteration technique"""
        for i in reversed(range(len(wall_h))):
            if wall_h[i] == 0:
                del wall_h[i]
                del wall_i[i]
    return water_sum
