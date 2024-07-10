def solution(clothes):
    from collections import defaultdict
    
    clothestype = defaultdict(list)
    for name, type in clothes:
        clothestype[type].append(name)
    
    combi = 1
    for type in clothestype:
        combi *= (len(clothestype[type]) + 1)
    
    return combi - 1