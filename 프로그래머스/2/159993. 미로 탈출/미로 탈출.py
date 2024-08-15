from collections import deque

def bfs(maps, start, goal):
    n, m = len(maps), len(maps[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    visited = [[False] * m for _ in range(n)]
    visited[start[0]][start[1]] = True
    distance = 0
    
    while queue:
        for i in range(len(queue)):
            x, y = queue.popleft()
            
            if (x, y) == goal:
                return distance
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        
        distance += 1
    
    return -1

def solution(maps):  
    n, m = len(maps), len(maps[0])
    
    start = lever = end = None
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)
    s_l = bfs(maps, start, lever)
    l_e = bfs(maps, lever, end)
    
    if s_l == -1 or l_e == -1:
        return -1

    return s_l + l_e