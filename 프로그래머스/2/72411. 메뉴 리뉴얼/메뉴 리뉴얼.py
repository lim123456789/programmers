from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for c in course:
        comb_count = Counter()
        for order in orders:
            comb_count.update(combinations(sorted(order), c))

        if comb_count:
            max_count = max(comb_count.values())
            if max_count > 1:
                for comb, cnt in comb_count.items():
                    if cnt == max_count:
                        answer.append(''.join(comb))
    
    return sorted(answer)