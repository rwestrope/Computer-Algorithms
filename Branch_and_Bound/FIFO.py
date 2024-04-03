from collections import deque

class Item:
    def __init__(self, value, weight):
        self.weight = weight
        self.value = value

def knapsack_BFS(items, capacity):
    queue = deque([(0, 0, 0)])  # (index, value, weight)

    best_value = 0

    while queue:
        index, value, weight = queue.popleft()

        if index >= len(items):
            if value > best_value:
                best_value = value
            continue

        # Include the item at the current index
        if weight + items[index].weight <= capacity:
            queue.append((index + 1, value + items[index].value, weight + items[index].weight))

        # Exclude the item at the current index
        queue.append((index + 1, value, weight))

    return best_value
