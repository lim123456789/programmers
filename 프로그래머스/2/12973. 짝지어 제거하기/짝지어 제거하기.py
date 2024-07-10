def solution(s):
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    return 1 if not stack else 0

if __name__ == "__main__":
    s = input("문자열 입력: ")
    print(solution(s))