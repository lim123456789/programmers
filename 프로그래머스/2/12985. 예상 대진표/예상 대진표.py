def solution(n,a,b):
    answer = 0
    
    while a != b:
        if a % 2 == 1:
            a += 1
        a /= 2
        
        if b % 2 == 1:
            b += 1
        b /= 2
        
        answer += 1

    return answer