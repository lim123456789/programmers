def hanoi(n, start, end, aux, result):
    if n == 1:
        result.append([start, end])
    else:
        hanoi(n - 1, start, aux, end, result)
        result.append([start, end])
        hanoi(n - 1, aux, end, start, result)


def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer