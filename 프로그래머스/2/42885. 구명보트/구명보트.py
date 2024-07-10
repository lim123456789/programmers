def solution(people, limit):
    answer = 0
    people.sort()
    left = 0
    right = len(people) - 1
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        answer += 1
        
    return answer

if __name__ == "__main__":
    people = list(map(int, input("사람들의 몸무게: ").split()))
    limit = int(input("무게 제한: "))
    print(solution(people, limit))