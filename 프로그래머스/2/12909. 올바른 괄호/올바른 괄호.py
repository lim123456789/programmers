def solution(s):
    answer = True
    stack=[]
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                answer=False
                break
    if stack:
        answer=False
        
    return answer

if __name__ == "__main__":
    s=input("")
    print(solution(s))