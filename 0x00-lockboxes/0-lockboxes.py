#!/usr/bin/python3
"""method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    lobo = set()
    keyly = set()
    keycur = 0
    """ make list of locked boxes in rep of numbers """
    for i in range(len(boxes)):
        lobo = lobo | {i}
    while len(keyly) < len(boxes):
        """ collect all the keys from the box that match the current key """
        for i in range(len(boxes[keycur])):
            if boxes[keycur][i] in lobo:
                keyly = keyly | {boxes[keycur][i]}
        boxes[keycur] = []
        """ search for the next useful key """
        lobo = lobo - {keycur}
        if len(lobo) == 0:
            return True
        if len(keyly & lobo) > 0:
            keycur = min((keyly & lobo))
        else:
            return False
    return True
