def isprime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    sqr = int(num ** 0.5) + 1    
    for i in range(3, sqr, 2):
        if num % i == 0:
            return False
    return True
        
    
def kbase(n, k):
    result = ""
    while n > 0:
        result = str(n % k) + result
        n = n // k
    return result

def solution(n, k):
    kstr = kbase(n, k)
    
    kk = kstr.split('0')
    
    prime_count = 0
    
    for kk in kk:
        if kk and isprime(int(kk)):
            prime_count += 1
            
    return prime_count