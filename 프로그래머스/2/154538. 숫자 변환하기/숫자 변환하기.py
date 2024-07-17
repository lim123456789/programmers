from collections import deque

def solution(x, y, n):
    queue = deque([(x, 0)])
    visited = set()
    visited.add(x)

    while queue:
        current, cal = queue.popleft()

        if current == y:
            return cal

        next_values = [current + n, current * 2, current * 3]
        
        for next_val in next_values:
            if next_val <= y and next_val not in visited:
                visited.add(next_val)
                queue.append((next_val, cal + 1))

    return -1