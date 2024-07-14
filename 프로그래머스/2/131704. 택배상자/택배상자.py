def solution(order):
    container = list(range(1, len(order) + 1))
    sub = []
    i = 0
    answer = 0
    
    for box in container:
        sub.append(box)
        
        while sub and sub[-1] == order[i]:
            sub.pop()
            i += 1
            answer += 1
            if i >= len(order):
                break
    return answer