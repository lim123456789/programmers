def convert(n, base):  
    digits = "0123456789ABCDEF"  
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = digits[n % base] + result  
        n = int(n / base)  
    return result

def solution(n, t, m, p):
    sequence = ""
    num = 0
    while len(sequence) < t * m:  
        sequence += convert(num, n) 
        num += 1
        
    result = ""
    for i in range(t):
        result += sequence[i * m + (p - 1)]  
    
    return result