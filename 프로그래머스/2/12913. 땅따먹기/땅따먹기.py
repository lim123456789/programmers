def solution(land):
    d = land[0]
    
    for i in range(1, len(land)):
        dd = [0] * 4
        for j in range(4):
            dd[j] = land[i][j] + max(d[k] for k in range(4) if k != j)
        d = dd

    return max(d)