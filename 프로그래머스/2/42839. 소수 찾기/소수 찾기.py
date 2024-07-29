from itertools import permutations

def isprime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    sqr = int(num ** 0.5) + 1    
    for i in range(3, sqr, 2):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    
    nnumbers = set()
    
    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i)
        for perm in perms:
            num = int(''.join(perm))
            nnumbers.add(num)
    answer = 0
    
    for num in nnumbers:
        if isprime(num):
            answer += 1
    return answer