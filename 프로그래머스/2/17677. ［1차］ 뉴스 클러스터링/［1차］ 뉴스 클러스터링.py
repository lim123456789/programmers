from collections import Counter
import re

def makemset(s):
    s = s.lower()
    mset = []
    for i in range(len(s) - 1):
        part = s[i:i + 2]
        if re.match(r'[a-z]{2}', part):
            mset.append(part)
    return mset

def solution(str1, str2):
    mset1 = makemset(str1)
    mset2 = makemset(str2)
    
    counter1 = Counter(mset1)
    counter2 = Counter(mset2)
    
    intersection = list((counter1 & counter2).elements())
    union = list((counter1 | counter2).elements())
    
    inter_len = len(intersection)
    union_len = len(union)
    
    if union_len == 0:
        jaccard = 1
    else:
        jaccard = inter_len / union_len

    return int(jaccard * 65536)