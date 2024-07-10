def solution(ph):
    ph.sort()
    for i in range(len(ph)-1):
        if ph[i+1].startswith(ph[i]):
            return False
    return True