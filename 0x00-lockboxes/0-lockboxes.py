#!/usr/bin/python3


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened."""

    if len(boxes) > 0:
        if len(boxes[0]) == 0:
            return False
        lobo = set()
        keyly = set()
        keycur = 0
        # make list of locked boxes in rep of numbers
        for i in range(len(boxes)):
            lobo = lobo | {i}
        while len(keyly) < len(boxes):
            # collect all the keys from the box that match the current key
            for i in range(len(boxes[keycur])):
                if boxes[keycur][i] in lobo:
                    keyly = keyly | {boxes[keycur][i]}
            keyly = set(keyly | {0})  # no dup
            boxes[keycur] = []
            # search for the next useful key
            lobo = lobo - {keycur}
            # if len(lobo) == 0:return True
            if len(keyly & lobo) > 0:
                keycur = min((keyly & lobo))
            else:
                return False
        return True
    return False
