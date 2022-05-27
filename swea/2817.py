# 부분 수열의 합

from itertools import combinations

t = int(input())

for i in range(1, t+1):
    print("#" + str(i), end=' ')  # TC 갯수

    n, k = map(int, input().split())    # n = 수열의 원소 개수, k = 부분 수열의 합
    A = list(map(int, input().split())) # 수열
    result = 0
    for j in range(1, n+1):
        for comb in combinations(A, j):
            if sum(comb) == k:
                result += 1
    print(result)