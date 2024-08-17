def solution(n, k):
    factorial = [1] * (n + 1)
    for i in range(2, n + 1):
        factorial[i] = factorial[i - 1] * i

    numbers = list(range(1, n + 1))
    result = []
    k -= 1
    
    for i in range(1, n + 1):
        idx = int(k / factorial[n - i])
        result.append(numbers[idx])
        numbers.pop(idx)
        k %= factorial[n - i]
    
    return result