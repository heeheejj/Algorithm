# [S/W 문제해결 기본] 1일차 - 최빈수 구하기

# import sys

# sys.stdin = open("input.txt", "r")

t = int(input())

for i in range(1, t+1):
    print("#"+input(), end=' ')
    scores = list(map(int, input().split()))
    fq = [0] * 101
    for score in scores:
        fq[score] += 1

    max_fq = max(fq)

    max_score = 0
    for i in range(len(fq)):
        if fq[i] == max_fq:
            max_score = max(max_score, i)
    print(max_score)