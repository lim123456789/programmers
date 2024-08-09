import math
from functools import reduce

def gcdl(l):
    return reduce(math.gcd, l)

def dist(gcd, array):
    return all(x % gcd != 0 for x in array)

def solution(arrayA, arrayB):
    answer = 0
    gcdA = gcdl(arrayA)
    gcdB = gcdl(arrayB)
    
    if dist(gcdA, arrayB):
        answer = max(answer, gcdA)
        
    if dist(gcdB, arrayA):
        answer = max(answer, gcdB)
    
    return answer