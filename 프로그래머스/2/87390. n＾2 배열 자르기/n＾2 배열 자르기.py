def solution(n, left, right):
    result = []
    for i in range(left, right + 1):
        x = int(i / n)
        y = int(i % n)
        value = max(x, y) + 1
        result.append(value)
    return result