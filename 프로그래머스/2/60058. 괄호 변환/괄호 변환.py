def solution(p):
    if not p:
        return p

    def split_balance(s):
        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            else:
                count -= 1
            if count == 0:
                return s[:i+1], s[i+1:]

    def is_correct(s):
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            else:
                if not stack:
                    return False
                stack.pop()
        return len(stack) == 0

    u, v = split_balance(p)
    
    if is_correct(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = u[1:-1]
        for char in u:
            if char == '(':
                answer += ')'
            else:
                answer += '('
        return answer