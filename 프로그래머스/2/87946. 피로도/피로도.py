from itertools import permutations

def solution(k, dungeons):
    maxex = 0
    
    for i in permutations(dungeons):
        hp = k
        explo = 0
        for dungeon in i:
            a, b = dungeon
            if hp >= a:
                hp -= b
                explo += 1
            else:
                break
        maxex = max(maxex, explo)
    
    return maxex