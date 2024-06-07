#!/usr/bin/python3
"""
Module Doc: Function to determine if all boxes can be unlocked

Attributes:
    boxes (List[List[int]]): list of boxes and their keys

Return:
    True if all boxes can be unlocked, else False
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.
    """

    if not boxes:
        return False

    num_boxes = len(boxes)
    unlocked = set([0])
    keys = set(boxes[0])

    while keys:
        new_keys = set()
        for key in keys:
            if key < num_boxes and key not in unlocked:
                unlocked.add(key)
                new_keys.update(boxes[key])
        keys = new_keys - unlocked

    return len(unlocked) == num_boxes
