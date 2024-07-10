def solution(s):

    s = s[2:-2]
    s = s.split("},{")

    sets = []
    for i in s:
        sets.append(list(map(int, i.split(','))))

    sets.sort(key=len)

    result = []
    for t in sets:
        for n in t:
            if n not in result:
                result.append(n)
    
    return result