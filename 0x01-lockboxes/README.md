# 0x01-lockboxes
This function takes a list of lists `boxes` as its input, where each inner list represents the keys contained in a box. It uses a stack-based approach to simulate opening the boxes one by one.

First, the function creates a list `unlocked_boxes` to keep track of which boxes are unlocked, with all elements initialized to `False` except for the first box `boxes[0]`. It also initializes a stack with the first box `0`.

Then, the function enters a loop that continues until the stack is empty. In each iteration, the function pops a box `box` from the top of the stack and iterates over the keys contained in that box using a `for` loop. For each key, the function checks if it corresponds to a valid box index (i.e., less than the total number of boxes `len(boxes)`) and if that box is currently locked (`unlocked_boxes[key] == False`). If both conditions are met, the function unlocks that box by setting `unlocked_boxes[key] = True` and adds it to the stack `stack.append(key)`.

Once the loop exits, the function returns `True` if all boxes are unlocked (i.e., all elements in `unlocked_boxes` are `True`), and `False` otherwise.
