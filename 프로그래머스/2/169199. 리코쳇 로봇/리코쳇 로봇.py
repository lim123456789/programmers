from collections import deque

def solution(board):
    n, m = len(board), len(board[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    start = None
    goal = None
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = (i, j)
            elif board[i][j] == 'G':
                goal = (i, j)

    queue = deque([(start[0], start[1], 0)])
    visited = set()
    visited.add(start)
    
    while queue:
        x, y, move_count = queue.popleft()

        if (x, y) == goal:
            return move_count

        for dx, dy in directions:
            nx, ny = x, y

            while 0 <= nx + dx < n and 0 <= ny + dy < m and board[nx + dx][ny + dy] != 'D':
                nx += dx
                ny += dy

            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, move_count + 1))

    return -1