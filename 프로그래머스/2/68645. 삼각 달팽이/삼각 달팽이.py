def solution(n):
    tri = [[0] * (i + 1) for i in range(n)]
    
    num = 1
    x, y = -1, 0
    for length in range(n):
        for a in range(length, n):
            if length % 3 == 0:
                x += 1
            elif length % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            tri[x][y] = num
            num += 1

    result = []
    for row in tri:
        result.extend(row)
    
    return result