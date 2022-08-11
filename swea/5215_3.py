# 햄버거 다이어트

from itertools import combinations

t = int(input())

for i in range(1, t+1):
    print("#" + str(i), end=' ')  # TC 갯수

    n, l = map(int, input().split())    # 재료의 수, 제한 칼로리
    inputs = list()
    for _ in range(n):
        t, k = map(int, input().split())
        inputs.append((t, k))

    t_sum_max = 0
    for j in range(1, n+1):
        for combs in list(combinations(inputs, j)):
            t_sum = 0
            k_sum = 0
            for comb in combs:
                t_sum += comb[0]
                k_sum += comb[1]
            if k_sum > l:
                continue
            else:
                t_sum_max = max(t_sum_max, t_sum)

    print(t_sum_max)