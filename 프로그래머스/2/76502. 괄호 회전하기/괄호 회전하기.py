def solution(s):
    
    n = len(s)
    count = 0

    bracket = {')': '(', ']': '[', '}': '{'}
    
    
    for i in range(n):
        rs = s[i:] + s[:i]
        stack = []
        valid = True
        
        for char in rs:
            if char in bracket.values():
                stack.append(char)
            elif char in bracket.keys():
                if stack == [] or bracket[char] != stack.pop():
                    valid = False
                    break
            else:
                valid = False
                break
                
        if valid and stack == []:
            count += 1
            
    return count