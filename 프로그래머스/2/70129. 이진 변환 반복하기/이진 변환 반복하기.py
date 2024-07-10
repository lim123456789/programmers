def solution(s):
    binarycnt = 0
    zerocnt = 0
    
    while s!="1":
        zerocnt = zerocnt + s.count('0')
        s = s.replace("0", "")
        
        length = len(s)
        s = bin(length)[2:]
        binarycnt = binarycnt + 1    
    
    
    return [binarycnt,zerocnt]

if __name__ == "__main__":
    s = input("문자열 입력: ")
    print(solution(s))