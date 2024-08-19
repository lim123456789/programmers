def check(place):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for r in range(5):
        for c in range(5):
            if place[r][c] == 'P':
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < 5 and 0 <= nc < 5 and place[nr][nc] == 'P':
                        return 0
                    if 0 <= nr < 5 and 0 <= nc < 5 and place[nr][nc] == 'O':
                        for dr2, dc2 in directions:
                            nr2, nc2 = nr + dr2, nc + dc2
                            if nr2 == r and nc2 == c:
                                continue
                            if 0 <= nr2 < 5 and 0 <= nc2 < 5 and place[nr2][nc2] == 'P':
                                return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer