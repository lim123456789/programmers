def solution(priorities, location):
    queue = [(priority, i) for i, priority in enumerate(priorities)]
    order = 0
    
    while queue:
        current = queue.pop(0)
        if any(current[0] < q[0] for q in queue):
            queue.append(current)
        else:
            order += 1
            if current[1] == location:
                return order