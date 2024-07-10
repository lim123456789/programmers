def solution(n):
    jump = [0] * (n + 2)
    jump [1] = 1
    jump [2] = 2
    
    if n <= 2:
        return jump [n] % 1234567
    else : 
        for i in range (3, n + 1):
            jump [i] = jump [i - 1] + jump [i - 2]
        return jump [n] % 1234567