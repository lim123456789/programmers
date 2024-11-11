from collections import Counter

def solution(n):
    ncount = Counter(n)
    mcv = ncount.most_common(1)[0]
    return mcv[0]


t = int(input())
for i in range(t):
    k = int(input())
    n = list(map(int, input().split()))
    result = solution(n)
    print(f"#{k} {result}")