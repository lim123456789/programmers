def solution(elements):
    
    exelements = elements * 2
    n = len(elements)
    
    allsum = set()
    
    for i in range(1, n + 1):
        for j in range(n):
            esum = sum(exelements[j:j + i])
            allsum.add(esum)
            
    return len(allsum)