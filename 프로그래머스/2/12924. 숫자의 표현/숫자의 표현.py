def solution(n):
    answer = 0
    for i in range(1, n + 1):
        check = 0
        for j in range(i, n + 1):
            check += j
            if check > n:
                break
            elif check == n:
                answer += 1
                break
    return answer

if __name__ == "__main__":
    n = int(input("숫자 입력: "))
    print(solution(s))