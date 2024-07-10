def solution(brown, yellow):
    size = brown + yellow
    
    for y in range(1, int(size**0.5) + 1):
        if size % y == 0:
            x = size / y
            if  (y - 2) * (x - 2) == yellow:
                return [x , y]
            
if __name__ == "__main__":
    brown, yellow = map(int, input("brown, yellow 입력: ").split())
    print(solution(brown, yellow))