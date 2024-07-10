def solution(n):
    answer = 0
    binn = bin(n)
    bincnt = binn.count('1')
    
    nextn = n + 1
    
    while(True):
        binnext = bin(nextn)
        nextcnt = binnext.count('1')
        if bincnt == nextcnt:
            answer = nextn
            break
        nextn += 1
    
    
    return answer

if __name__ == "__main__":
    n = int(input("자연수 입력: "))
    print(solution(s))