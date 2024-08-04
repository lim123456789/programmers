from collections import Counter

def solution(weights):
    answer = 0
    wc = Counter(weights)
    d = [2, 3, 4]

    for weight in wc:
        count = wc[weight]
        if count > 1:
            answer += count * (count - 1) // 2

    for w1 in wc:
        for w2 in wc:
            if w1 < w2:
                for d1 in d:
                    for d2 in d:
                        if w1 * d1 == w2 * d2:
                            answer += wc[w1] * wc[w2]
    
    return answer