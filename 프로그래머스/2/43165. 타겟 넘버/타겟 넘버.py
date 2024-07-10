def solution(numbers, target):
    def dfs(current_sum, index):
        if index == len(numbers):
            return 1 if current_sum == target else 0
        return dfs(current_sum + numbers[index], index + 1) + dfs(current_sum - numbers[index], index + 1)
    
    return dfs(0, 0)