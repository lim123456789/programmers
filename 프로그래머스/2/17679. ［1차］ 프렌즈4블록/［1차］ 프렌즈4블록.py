def solution(m, n, board):
    board = [list(i) for i in board]

    def find_2x2():
        remove = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != '':
                    remove.add((i, j))
                    remove.add((i, j+1))
                    remove.add((i+1, j))
                    remove.add((i+1, j+1))
        return remove

    def remove_blocks(remove):
        for i, j in remove:
            board[i][j] = ''
        return len(remove)

    def drop_blocks():
        for j in range(n):
            empty = m - 1
            for i in range(m - 1, -1, -1):
                if board[i][j] != '':
                    board[empty][j] = board[i][j]
                    if empty != i:
                        board[i][j] = ''
                    empty -= 1

    total_removed = 0
    while True:
        remove = find_2x2()
        if not remove:
            break
        total_removed += remove_blocks(remove)
        drop_blocks()

    return total_removed