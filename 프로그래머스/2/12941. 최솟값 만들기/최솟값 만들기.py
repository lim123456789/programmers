def solution(A,B):
    answer = 0

    A.sort(reverse=False)
    B.sort(reverse=True)
    
    for i in range(len(A)):
        answer=answer+(A[i]*B[i])
    return answer

if __name__ == "__main__":
    A = list(map(int, input("A 리스트 입력 (공백으로 구분): ").split()))
    B = list(map(int, input("B 리스트 입력 (공백으로 구분): ").split()))
    print(solution(A,B))