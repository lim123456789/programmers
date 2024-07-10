def solution(msg):
    dictionary = {chr(i): i - 64 for i in range(65, 91)}
    dict_size = 27
    w = ""
    result = []
    
    for c in msg:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
    
    if w:
        result.append(dictionary[w])
    
    return result