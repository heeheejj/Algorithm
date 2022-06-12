def solution(p):
    n = len(p)
    i = 0
    j = 0
    m = 9999
    answer = [0] * n
    if p == sorted(p):
        return answer
    while i < n:
        m = min(p[i:])
        for k in range(i, n):
            if m == p[k]:
                j = k
        if j != i:
            p[i], p[j] = p[j], p[i]
            answer[i] += 1
            answer[j] += 1
            print(p)
        i += 1
        if i == n:
            return answer