def solution(s):
    answer = ''
    numbers = s.split()
    numbers = list(map(int, numbers))
    
    min_value = min(numbers)
    max_value = max(numbers)
    
    answer = f"{min_value} {max_value}"
    return answer

if __name__ == "__main__":
    s = input("")
    print(solution(s))