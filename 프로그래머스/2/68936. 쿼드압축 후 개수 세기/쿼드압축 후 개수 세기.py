def solution(arr):
    def compress(x, y, size):
        initial = arr[x][y]
        all_same = True

        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != initial:
                    all_same = False
                    break
            if not all_same:
                break

        if all_same:
            return (1, 0) if initial == 0 else (0, 1)

        half = size // 2
        top_left = compress(x, y, half)
        top_right = compress(x, y + half, half)
        bottom_left = compress(x + half, y, half)
        bottom_right = compress(x + half, y + half, half)

        zero_count = top_left[0] + top_right[0] + bottom_left[0] + bottom_right[0]
        one_count = top_left[1] + top_right[1] + bottom_left[1] + bottom_right[1]
        return (zero_count, one_count)

    return list(compress(0, 0, len(arr)))