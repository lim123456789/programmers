def solution(sequence, k):
    n = len(sequence)
    sp, ep = 0, 0
    cs = sequence[0]
    ml = float('inf')
    answer = []

    while sp < n and ep < n:
        if cs == k:
            if ep - sp < ml:
                ml = ep - sp
                answer = [sp, ep]
            cs -= sequence[sp]
            sp += 1
        elif cs < k:
            ep += 1
            if ep < n:
                cs += sequence[ep]
        else:
            cs -= sequence[sp]
            sp += 1

    return answer