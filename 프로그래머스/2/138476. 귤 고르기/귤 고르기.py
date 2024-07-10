from collections import Counter

def solution(k, tangerine):
    tcount = Counter(tangerine)

    tsort = sorted(tcount.values(), reverse=True)
    
    count = 0
    total = 0
    
    for i in tsort:
        total += i
        count += 1
        if total >= k:
            break
            
    return count