#!/usr/bin/python3
"""A method that determines if all the boxes can be opened."""
def canUnlockAll(boxes):
    unlocked_boxes = [False] * len(boxes)
    unlocked_boxes[0] = True
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < len(boxes) and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                stack.append(key)

    return all(unlocked_boxes)

