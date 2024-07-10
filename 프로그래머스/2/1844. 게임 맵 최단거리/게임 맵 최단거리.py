from collections import deque

def solution(maps):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    n, m = len(maps), len(maps[0])

    queue = deque([(0, 0, 1)])

    while queue:
        x, y, dist = queue.popleft()

        if x == n - 1 and y == m - 1:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                queue.append((nx, ny, dist + 1))
                maps[nx][ny] = 0

    return -1