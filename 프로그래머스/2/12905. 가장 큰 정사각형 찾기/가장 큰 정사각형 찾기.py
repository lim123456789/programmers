def solution(board):
    answer = 0

    n, m = len(board), len(board[0])
    dp = [[0] * m for x in range(n)]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                answer = max(answer, dp[i][j])

    return answer ** 2