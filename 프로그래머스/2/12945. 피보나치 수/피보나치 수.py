def solution(n):
    answer = 0
    
    if n <= 1:
        answer = 1
    
    else:
        a = 0
        b = 1
        for i in range(2, n + 1):
            answer = (a + b) % 1234567
            a = b % 1234567
            b = answer
        
    return answer

if __name__ == "__main__":
    n = int(input("숫자 입력: "))
    print(solution(s))